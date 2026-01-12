from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from datetime import datetime, timedelta
from email_validator import validate_email, EmailNotValidError
import re
import uuid

from config import Config
from models import db, User, PasswordResetToken

app = Flask(__name__)
app.config.from_object(Config)

# Initialize extensions
CORS(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
db.init_app(app)

# Create tables
with app.app_context():
    db.create_all()

# Helper functions
def validate_password(password):
    """Validate password strength"""
    if len(password) < 8:
        return False, "Mật khẩu phải có ít nhất 8 ký tự"
    if not re.search(r"[A-Z]", password):
        return False, "Mật khẩu phải có ít nhất 1 chữ in hoa"
    if not re.search(r"[a-z]", password):
        return False, "Mật khẩu phải có ít nhất 1 chữ thường"
    if not re.search(r"\d", password):
        return False, "Mật khẩu phải có ít nhất 1 số"
    return True, "Valid"

def validate_phone(phone):
    """Validate Vietnamese phone number"""
    if not phone:
        return True  # Phone is optional
    pattern = r'^(0[3|5|7|8|9])+([0-9]{8})$'
    return bool(re.match(pattern, phone))

# Routes
@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'success',
        'message': 'Drink Shop API is running',
        'timestamp': datetime.utcnow().isoformat()
    }), 200

@app.route('/api/register', methods=['POST'])
def register():
    """Register a new user"""
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['email', 'username', 'password', 'full_name']
        for field in required_fields:
            if not data.get(field):
                return jsonify({
                    'status': 'error',
                    'message': f'Trường {field} là bắt buộc'
                }), 400
        
        email = data.get('email').strip().lower()
        username = data.get('username').strip().lower()
        password = data.get('password')
        full_name = data.get('full_name').strip()
        phone = data.get('phone', '').strip()
        
        # Validate email
        try:
            valid = validate_email(email)
            email = valid.email
        except EmailNotValidError as e:
            return jsonify({
                'status': 'error',
                'message': 'Email không hợp lệ'
            }), 400
        
        # Validate username
        if len(username) < 3:
            return jsonify({
                'status': 'error',
                'message': 'Tên đăng nhập phải có ít nhất 3 ký tự'
            }), 400
        
        if not re.match(r'^[a-z0-9_]+$', username):
            return jsonify({
                'status': 'error',
                'message': 'Tên đăng nhập chỉ được chứa chữ thường, số và dấu gạch dưới'
            }), 400
        
        # Validate password
        is_valid, message = validate_password(password)
        if not is_valid:
            return jsonify({
                'status': 'error',
                'message': message
            }), 400
        
        # Validate phone
        if phone and not validate_phone(phone):
            return jsonify({
                'status': 'error',
                'message': 'Số điện thoại không hợp lệ'
            }), 400
        
        # Check if email exists
        if User.query.filter_by(email=email).first():
            return jsonify({
                'status': 'error',
                'message': 'Email đã được sử dụng'
            }), 400
        
        # Check if username exists
        if User.query.filter_by(username=username).first():
            return jsonify({
                'status': 'error',
                'message': 'Tên đăng nhập đã được sử dụng'
            }), 400
        
        # Hash password
        password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
        
        # Create new user
        new_user = User(
            email=email,
            username=username,
            password_hash=password_hash,
            full_name=full_name,
            phone=phone if phone else None
        )
        
        db.session.add(new_user)
        db.session.commit()
        
        # Generate access token
        access_token = create_access_token(identity=new_user.id)
        
        return jsonify({
            'status': 'success',
            'message': 'Đăng ký thành công',
            'data': {
                'user': new_user.to_dict(),
                'access_token': access_token
            }
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'status': 'error',
            'message': f'Đã xảy ra lỗi: {str(e)}'
        }), 500

@app.route('/api/login', methods=['POST'])
def login():
    """Login user"""
    try:
        data = request.get_json()
        
        # Validate required fields
        if not data.get('login') or not data.get('password'):
            return jsonify({
                'status': 'error',
                'message': 'Email/Username và mật khẩu là bắt buộc'
            }), 400
        
        login_value = data.get('login').strip().lower()
        password = data.get('password')
        
        # Find user by email or username
        user = User.query.filter(
            (User.email == login_value) | (User.username == login_value)
        ).first()
        
        if not user:
            return jsonify({
                'status': 'error',
                'message': 'Email/Username hoặc mật khẩu không đúng'
            }), 401
        
        # Check if user is active
        if not user.is_active:
            return jsonify({
                'status': 'error',
                'message': 'Tài khoản đã bị khóa'
            }), 403
        
        # Verify password
        if not bcrypt.check_password_hash(user.password_hash, password):
            return jsonify({
                'status': 'error',
                'message': 'Email/Username hoặc mật khẩu không đúng'
            }), 401
        
        # Generate access token
        access_token = create_access_token(identity=user.id)
        
        return jsonify({
            'status': 'success',
            'message': 'Đăng nhập thành công',
            'data': {
                'user': user.to_dict(),
                'access_token': access_token
            }
        }), 200
        
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f'Đã xảy ra lỗi: {str(e)}'
        }), 500

@app.route('/api/forgot-password', methods=['POST'])
def forgot_password():
    """Send password reset email"""
    try:
        data = request.get_json()
        
        # Validate required fields
        if not data.get('email'):
            return jsonify({
                'status': 'error',
                'message': 'Email là bắt buộc'
            }), 400
        
        email = data.get('email').strip().lower()
        
        # Validate email
        try:
            valid = validate_email(email)
            email = valid.email
        except EmailNotValidError:
            return jsonify({
                'status': 'error',
                'message': 'Email không hợp lệ'
            }), 400
        
        # Find user
        user = User.query.filter_by(email=email).first()
        
        # Always return success message (security best practice)
        # Don't reveal if email exists or not
        if user and user.is_active:
            # Generate reset token
            reset_token = str(uuid.uuid4())
            expires_at = datetime.utcnow() + timedelta(hours=1)
            
            # Save token to database
            password_reset = PasswordResetToken(
                user_id=user.id,
                token=reset_token,
                expires_at=expires_at
            )
            db.session.add(password_reset)
            db.session.commit()
            
            # In production, send email here
            # For now, just log the token (for development)
            print(f"Password reset token for {email}: {reset_token}")
            print(f"Reset link: http://localhost:3000/reset-password?token={reset_token}")
        
        return jsonify({
            'status': 'success',
            'message': 'Nếu email tồn tại trong hệ thống, bạn sẽ nhận được email khôi phục mật khẩu'
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'status': 'error',
            'message': f'Đã xảy ra lỗi: {str(e)}'
        }), 500

@app.route('/api/reset-password', methods=['POST'])
def reset_password():
    """Reset password with token"""
    try:
        data = request.get_json()
        
        # Validate required fields
        if not data.get('token') or not data.get('new_password'):
            return jsonify({
                'status': 'error',
                'message': 'Token và mật khẩu mới là bắt buộc'
            }), 400
        
        token = data.get('token')
        new_password = data.get('new_password')
        
        # Validate password
        is_valid, message = validate_password(new_password)
        if not is_valid:
            return jsonify({
                'status': 'error',
                'message': message
            }), 400
        
        # Find token
        reset_token = PasswordResetToken.query.filter_by(
            token=token,
            is_used=False
        ).first()
        
        if not reset_token:
            return jsonify({
                'status': 'error',
                'message': 'Token không hợp lệ hoặc đã được sử dụng'
            }), 400
        
        # Check if token expired
        if datetime.utcnow() > reset_token.expires_at:
            return jsonify({
                'status': 'error',
                'message': 'Token đã hết hạn'
            }), 400
        
        # Get user
        user = User.query.get(reset_token.user_id)
        if not user:
            return jsonify({
                'status': 'error',
                'message': 'Người dùng không tồn tại'
            }), 404
        
        # Update password
        user.password_hash = bcrypt.generate_password_hash(new_password).decode('utf-8')
        reset_token.is_used = True
        
        db.session.commit()
        
        return jsonify({
            'status': 'success',
            'message': 'Đặt lại mật khẩu thành công'
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'status': 'error',
            'message': f'Đã xảy ra lỗi: {str(e)}'
        }), 500

@app.route('/api/profile', methods=['GET'])
@jwt_required()
def get_profile():
    """Get current user profile"""
    try:
        current_user_id = get_jwt_identity()
        user = User.query.get(current_user_id)
        
        if not user:
            return jsonify({
                'status': 'error',
                'message': 'Người dùng không tồn tại'
            }), 404
        
        return jsonify({
            'status': 'success',
            'data': user.to_dict()
        }), 200
        
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f'Đã xảy ra lỗi: {str(e)}'
        }), 500

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'status': 'error',
        'message': 'Endpoint không tồn tại'
    }), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return jsonify({
        'status': 'error',
        'message': 'Lỗi máy chủ nội bộ'
    }), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
