# 🍹 Drink Shop - Authentication System

Hệ thống xác thực (Authentication) hoàn chỉnh cho website Drink Shop với giao diện hiện đại, sang trọng sử dụng màu vàng (Amber) làm chủ đạo.

## 🎨 Thiết kế UI/UX

- **Phong cách**: Hiện đại, sạch sẽ, sang trọng
- **Màu sắc chủ đạo**: Vàng/Amber (#f59e0b) kết hợp với Trắng và Đen
- **Hiệu ứng**: Card bo góc, shadow mềm mại, hover animations mượt mà
- **Icons**: Sử dụng Lucide React cho icons sắc nét
- **Responsive**: Hoạt động hoàn hảo trên cả Desktop và Mobile

## 🚀 Tính năng

### 1. **Login (Đăng nhập)**
- Form đăng nhập với Email/Username và Password
- Hiển thị/Ẩn mật khẩu
- Social Login buttons (Google, Facebook, Github) - UI only
- Link "Quên mật khẩu"
- Ghi nhớ đăng nhập
- Validation và error handling

### 2. **Register (Đăng ký)**
- Form đăng ký với đầy đủ thông tin: Họ tên, Email, Username, Số điện thoại, Mật khẩu
- Password strength indicator (Độ mạnh mật khẩu)
- Xác nhận mật khẩu với hiển thị match status
- Social Registration buttons
- Validation theo tiêu chuẩn:
  - Email hợp lệ
  - Username: chữ thường, số, gạch dưới, tối thiểu 3 ký tự
  - Password: tối thiểu 8 ký tự, có chữ hoa, chữ thường, số
  - Phone: Format số điện thoại Việt Nam

### 3. **Forgot Password (Quên mật khẩu)**
- Form nhập email để nhận link khôi phục
- Success message với hướng dẫn chi tiết
- Thông báo kiểm tra spam folder
- Có thể gửi lại email

### 4. **Dashboard**
- Trang hiển thị thông tin user sau khi đăng nhập thành công
- Hiển thị thông tin tài khoản
- Nút đăng xuất

## 🛠️ Tech Stack

### Frontend
- **React.js 18** - UI Library
- **Vite** - Build tool
- **Tailwind CSS 3** - Styling framework
- **React Router DOM 6** - Routing
- **Axios** - HTTP client
- **Lucide React** - Icon library

### Backend
- **Python Flask 3** - Web framework
- **Flask-SQLAlchemy** - ORM
- **Flask-Bcrypt** - Password hashing
- **Flask-JWT-Extended** - JWT authentication
- **Flask-CORS** - CORS handling
- **SQLite** - Database
- **Email-validator** - Email validation

## 📁 Cấu trúc Project

```
backend1/
├── backend/
│   ├── app.py              # Flask application
│   ├── models.py           # Database models
│   ├── config.py           # Configuration
│   ├── requirements.txt    # Python dependencies
│   └── .env.example        # Environment variables example
│
└── frontend/
    ├── src/
    │   ├── pages/
    │   │   ├── Login.jsx           # Login component
    │   │   ├── Register.jsx        # Register component
    │   │   ├── ForgotPassword.jsx  # Forgot password component
    │   │   └── Dashboard.jsx       # Dashboard component
    │   ├── services/
    │   │   └── api.js              # API service
    │   ├── App.jsx                 # Main app component
    │   ├── main.jsx                # Entry point
    │   └── index.css               # Global styles
    ├── index.html
    ├── package.json
    ├── vite.config.js
    ├── tailwind.config.js
    └── postcss.config.js
```

## 🔧 Cài đặt và Chạy

### Backend (Flask API)

1. Di chuyển vào thư mục backend:
```bash
cd d:\backend1
```

2. Tạo và kích hoạt virtual environment:
```bash
python -m venv venv
.\venv\Scripts\activate
```

3. Cài đặt dependencies:
```bash
pip install -r requirements.txt
```

4. Tạo file `.env` từ `.env.example`:
```bash
Copy-Item .env.example .env
```

5. Chạy Flask server:
```bash
python app.py
```

Server sẽ chạy tại: `http://localhost:5000`

### Frontend (React)

1. Di chuyển vào thư mục frontend:
```bash
cd d:\backend1\frontend
```

2. Cài đặt dependencies:
```bash
npm install
```

3. Chạy development server:
```bash
npm run dev
```

Frontend sẽ chạy tại: `http://localhost:3000`

## 🌐 API Endpoints

### Health Check
- `GET /api/health` - Kiểm tra trạng thái API

### Authentication
- `POST /api/register` - Đăng ký tài khoản mới
- `POST /api/login` - Đăng nhập
- `POST /api/forgot-password` - Gửi email khôi phục mật khẩu
- `POST /api/reset-password` - Đặt lại mật khẩu
- `GET /api/profile` - Lấy thông tin user (cần JWT token)

### Request/Response Examples

#### Register
**Request:**
```json
POST /api/register
{
  "email": "user@example.com",
  "username": "username",
  "password": "Password123",
  "full_name": "Nguyen Van A",
  "phone": "0912345678"
}
```

**Response:**
```json
{
  "status": "success",
  "message": "Đăng ký thành công",
  "data": {
    "user": {
      "id": "uuid",
      "email": "user@example.com",
      "username": "username",
      "full_name": "Nguyen Van A",
      "phone": "0912345678"
    },
    "access_token": "jwt_token_here"
  }
}
```

#### Login
**Request:**
```json
POST /api/login
{
  "login": "user@example.com",
  "password": "Password123"
}
```

**Response:**
```json
{
  "status": "success",
  "message": "Đăng nhập thành công",
  "data": {
    "user": { ... },
    "access_token": "jwt_token_here"
  }
}
```

## 🎯 Tính năng nổi bật

### Frontend
- ✅ Responsive design hoàn hảo
- ✅ Loading states cho tất cả actions
- ✅ Error handling với UI đẹp mắt
- ✅ Password strength indicator
- ✅ Show/Hide password functionality
- ✅ Social login buttons (UI ready)
- ✅ Protected routes với JWT
- ✅ Smooth animations và transitions
- ✅ Form validation real-time

### Backend
- ✅ JWT authentication
- ✅ Password hashing với Bcrypt
- ✅ Email validation
- ✅ Vietnamese phone validation
- ✅ Password strength validation
- ✅ CORS enabled
- ✅ Error handling middleware
- ✅ Database models với SQLAlchemy
- ✅ Password reset token system

## 🔐 Security Features

- Password hashing với Bcrypt
- JWT token authentication
- Password strength requirements
- Email validation
- CORS protection
- SQL injection protection (SQLAlchemy ORM)
- XSS protection
- Token expiration (1 hour)

## 🎨 Color Palette

```
Primary (Amber):
- 50:  #fffbeb
- 100: #fef3c7
- 200: #fde68a
- 300: #fcd34d
- 400: #fbbf24
- 500: #f59e0b (Main)
- 600: #d97706
- 700: #b45309
- 800: #92400e
- 900: #78350f
```

## 📱 Screenshots Preview

### Login Page
- Clean and modern login form
- Social login buttons
- Remember me checkbox
- Forgot password link

### Register Page
- Comprehensive registration form
- Password strength indicator
- Real-time validation
- Terms and conditions

### Forgot Password Page
- Simple email input
- Success message with instructions
- Resend email option

### Dashboard
- Welcome message
- User information display
- Logout functionality

## 🚧 Phát triển tiếp

- [ ] Implement actual social login (Google, Facebook, Github OAuth)
- [ ] Email service integration cho forgot password
- [ ] Two-factor authentication (2FA)
- [ ] User profile editing
- [ ] Account settings page
- [ ] Admin dashboard
- [ ] User role management

## 📝 License

© 2026 Drink Shop. All rights reserved.

---

**Developed with ❤️ for Drink Shop**
