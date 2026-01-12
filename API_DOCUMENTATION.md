# 🔌 Drink Shop - API Documentation

Base URL: `http://localhost:5000/api`

---

## 📋 Table of Contents

1. [Health Check](#health-check)
2. [Register](#register)
3. [Login](#login)
4. [Forgot Password](#forgot-password)
5. [Reset Password](#reset-password)
6. [Get Profile](#get-profile)
7. [Error Responses](#error-responses)

---

## Health Check

Kiểm tra trạng thái hoạt động của API.

### Endpoint
```
GET /api/health
```

### Headers
```
Content-Type: application/json
```

### Response
```json
{
  "status": "success",
  "message": "Drink Shop API is running",
  "timestamp": "2026-01-12T10:30:00.000000"
}
```

### Status Codes
- `200 OK` - API đang hoạt động

---

## Register

Đăng ký tài khoản người dùng mới.

### Endpoint
```
POST /api/register
```

### Headers
```
Content-Type: application/json
```

### Request Body
```json
{
  "email": "user@example.com",
  "username": "username",
  "password": "Password123",
  "full_name": "Nguyen Van A",
  "phone": "0912345678"
}
```

### Parameters

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| email | string | Yes | Email hợp lệ |
| username | string | Yes | Tên đăng nhập (chữ thường, số, gạch dưới, min 3 ký tự) |
| password | string | Yes | Mật khẩu (min 8 ký tự, có chữ hoa, thường, số) |
| full_name | string | Yes | Họ và tên đầy đủ |
| phone | string | No | Số điện thoại (format VN: 09/03/05/07/08 + 8 số) |

### Validation Rules

**Email:**
- Phải là email hợp lệ
- Chưa tồn tại trong hệ thống

**Username:**
- Độ dài: tối thiểu 3 ký tự
- Ký tự: chỉ chữ thường (a-z), số (0-9), gạch dưới (_)
- Chưa tồn tại trong hệ thống

**Password:**
- Độ dài: tối thiểu 8 ký tự
- Phải có ít nhất 1 chữ in hoa (A-Z)
- Phải có ít nhất 1 chữ thường (a-z)
- Phải có ít nhất 1 số (0-9)

**Phone (Optional):**
- Format: 10 số
- Bắt đầu với: 03, 05, 07, 08, 09
- Pattern: `^(0[3|5|7|8|9])+([0-9]{8})$`

### Success Response (201 Created)
```json
{
  "status": "success",
  "message": "Đăng ký thành công",
  "data": {
    "user": {
      "id": "550e8400-e29b-41d4-a716-446655440000",
      "email": "user@example.com",
      "username": "username",
      "full_name": "Nguyen Van A",
      "phone": "0912345678",
      "is_active": true,
      "created_at": "2026-01-12T10:30:00.000000"
    },
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
  }
}
```

### Error Responses

**400 Bad Request - Missing Field:**
```json
{
  "status": "error",
  "message": "Trường email là bắt buộc"
}
```

**400 Bad Request - Invalid Email:**
```json
{
  "status": "error",
  "message": "Email không hợp lệ"
}
```

**400 Bad Request - Email Exists:**
```json
{
  "status": "error",
  "message": "Email đã được sử dụng"
}
```

**400 Bad Request - Username Exists:**
```json
{
  "status": "error",
  "message": "Tên đăng nhập đã được sử dụng"
}
```

**400 Bad Request - Weak Password:**
```json
{
  "status": "error",
  "message": "Mật khẩu phải có ít nhất 8 ký tự"
}
```

**400 Bad Request - Invalid Phone:**
```json
{
  "status": "error",
  "message": "Số điện thoại không hợp lệ"
}
```

### cURL Example
```bash
curl -X POST http://localhost:5000/api/register \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "username": "username",
    "password": "Password123",
    "full_name": "Nguyen Van A",
    "phone": "0912345678"
  }'
```

---

## Login

Đăng nhập vào hệ thống.

### Endpoint
```
POST /api/login
```

### Headers
```
Content-Type: application/json
```

### Request Body
```json
{
  "login": "user@example.com",
  "password": "Password123"
}
```

### Parameters

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| login | string | Yes | Email hoặc Username |
| password | string | Yes | Mật khẩu |

### Success Response (200 OK)
```json
{
  "status": "success",
  "message": "Đăng nhập thành công",
  "data": {
    "user": {
      "id": "550e8400-e29b-41d4-a716-446655440000",
      "email": "user@example.com",
      "username": "username",
      "full_name": "Nguyen Van A",
      "phone": "0912345678",
      "is_active": true,
      "created_at": "2026-01-12T10:30:00.000000"
    },
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
  }
}
```

### Error Responses

**400 Bad Request - Missing Fields:**
```json
{
  "status": "error",
  "message": "Email/Username và mật khẩu là bắt buộc"
}
```

**401 Unauthorized - Invalid Credentials:**
```json
{
  "status": "error",
  "message": "Email/Username hoặc mật khẩu không đúng"
}
```

**403 Forbidden - Account Inactive:**
```json
{
  "status": "error",
  "message": "Tài khoản đã bị khóa"
}
```

### cURL Example
```bash
curl -X POST http://localhost:5000/api/login \
  -H "Content-Type: application/json" \
  -d '{
    "login": "user@example.com",
    "password": "Password123"
  }'
```

---

## Forgot Password

Gửi email khôi phục mật khẩu.

### Endpoint
```
POST /api/forgot-password
```

### Headers
```
Content-Type: application/json
```

### Request Body
```json
{
  "email": "user@example.com"
}
```

### Parameters

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| email | string | Yes | Email đã đăng ký |

### Success Response (200 OK)
```json
{
  "status": "success",
  "message": "Nếu email tồn tại trong hệ thống, bạn sẽ nhận được email khôi phục mật khẩu"
}
```

**Note:** Response luôn trả về success để tránh information disclosure attack (không tiết lộ email có tồn tại hay không).

### Error Responses

**400 Bad Request - Missing Email:**
```json
{
  "status": "error",
  "message": "Email là bắt buộc"
}
```

**400 Bad Request - Invalid Email:**
```json
{
  "status": "error",
  "message": "Email không hợp lệ"
}
```

### Behind the Scenes

Nếu email tồn tại trong hệ thống:
1. Tạo reset token (UUID)
2. Lưu token vào database với thời gian hết hạn (1 giờ)
3. Token được in ra console (trong development)
4. Trong production: Gửi email với link reset

**Console Output (Development):**
```
Password reset token for user@example.com: 550e8400-e29b-41d4-a716-446655440000
Reset link: http://localhost:3000/reset-password?token=550e8400-e29b-41d4-a716-446655440000
```

### cURL Example
```bash
curl -X POST http://localhost:5000/api/forgot-password \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com"
  }'
```

---

## Reset Password

Đặt lại mật khẩu với token từ email.

### Endpoint
```
POST /api/reset-password
```

### Headers
```
Content-Type: application/json
```

### Request Body
```json
{
  "token": "550e8400-e29b-41d4-a716-446655440000",
  "new_password": "NewPassword123"
}
```

### Parameters

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| token | string | Yes | Reset token từ email |
| new_password | string | Yes | Mật khẩu mới (min 8 ký tự, có chữ hoa, thường, số) |

### Success Response (200 OK)
```json
{
  "status": "success",
  "message": "Đặt lại mật khẩu thành công"
}
```

### Error Responses

**400 Bad Request - Missing Fields:**
```json
{
  "status": "error",
  "message": "Token và mật khẩu mới là bắt buộc"
}
```

**400 Bad Request - Weak Password:**
```json
{
  "status": "error",
  "message": "Mật khẩu phải có ít nhất 8 ký tự"
}
```

**400 Bad Request - Invalid/Used Token:**
```json
{
  "status": "error",
  "message": "Token không hợp lệ hoặc đã được sử dụng"
}
```

**400 Bad Request - Expired Token:**
```json
{
  "status": "error",
  "message": "Token đã hết hạn"
}
```

**404 Not Found - User Not Found:**
```json
{
  "status": "error",
  "message": "Người dùng không tồn tại"
}
```

### cURL Example
```bash
curl -X POST http://localhost:5000/api/reset-password \
  -H "Content-Type: application/json" \
  -d '{
    "token": "550e8400-e29b-41d4-a716-446655440000",
    "new_password": "NewPassword123"
  }'
```

---

## Get Profile

Lấy thông tin user hiện tại (yêu cầu authentication).

### Endpoint
```
GET /api/profile
```

### Headers
```
Content-Type: application/json
Authorization: Bearer <access_token>
```

### Success Response (200 OK)
```json
{
  "status": "success",
  "data": {
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "email": "user@example.com",
    "username": "username",
    "full_name": "Nguyen Van A",
    "phone": "0912345678",
    "is_active": true,
    "created_at": "2026-01-12T10:30:00.000000"
  }
}
```

### Error Responses

**401 Unauthorized - Missing Token:**
```json
{
  "msg": "Missing Authorization Header"
}
```

**401 Unauthorized - Invalid Token:**
```json
{
  "msg": "Invalid token"
}
```

**401 Unauthorized - Expired Token:**
```json
{
  "msg": "Token has expired"
}
```

**404 Not Found - User Not Found:**
```json
{
  "status": "error",
  "message": "Người dùng không tồn tại"
}
```

### cURL Example
```bash
curl -X GET http://localhost:5000/api/profile \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
```

---

## Error Responses

### General Error Format
```json
{
  "status": "error",
  "message": "Error description in Vietnamese"
}
```

### Status Codes

| Code | Meaning | Usage |
|------|---------|-------|
| 200 | OK | Successful GET/POST request |
| 201 | Created | Successfully created resource (register) |
| 400 | Bad Request | Validation error, missing fields |
| 401 | Unauthorized | Invalid credentials, missing/invalid token |
| 403 | Forbidden | Account locked/disabled |
| 404 | Not Found | Resource not found |
| 500 | Internal Server Error | Server-side error |

### Common Error Scenarios

**Network Error (Frontend):**
```json
{
  "message": "Network Error"
}
```

**CORS Error:**
- Ensure backend is running
- Check CORS configuration in Flask

**Token Expired:**
```json
{
  "msg": "Token has expired"
}
```
Action: Redirect to login page, clear localStorage

---

## JWT Token

### Token Format
```
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcwNTE...
```

### Token Payload (Decoded)
```json
{
  "fresh": false,
  "iat": 1705123456,
  "jti": "550e8400-e29b-41d4-a716-446655440000",
  "type": "access",
  "sub": "user-id-here",
  "nbf": 1705123456,
  "exp": 1705127056
}
```

### Token Lifetime
- **Access Token:** 1 hour (3600 seconds)

### Using Token in Requests

**Header:**
```
Authorization: Bearer <access_token>
```

**JavaScript (Axios):**
```javascript
axios.get('/api/profile', {
  headers: {
    'Authorization': `Bearer ${localStorage.getItem('access_token')}`
  }
})
```

---

## Rate Limiting

Currently: **No rate limiting** (for development)

Recommended for production:
- Login: 5 requests per minute per IP
- Register: 3 requests per minute per IP
- Forgot Password: 2 requests per minute per IP
- API calls: 100 requests per minute per user

---

## Security Considerations

### Password Hashing
- Algorithm: **Bcrypt**
- Work factor: Default (12 rounds)
- Salt: Automatically generated per password

### Token Security
- Store in: localStorage (frontend)
- Send via: Authorization header
- Never: Send in URL params
- HTTPS: Required in production

### CORS
- Allowed Origins: `http://localhost:3000` (development)
- Production: Configure specific domains

### SQL Injection
- Protection: SQLAlchemy ORM (parameterized queries)

### XSS Protection
- React: Auto-escapes output
- Never use: `dangerouslySetInnerHTML` with user input

---

## Testing Endpoints

### Postman Collection

Import this JSON to Postman:

```json
{
  "info": {
    "name": "Drink Shop API",
    "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
  },
  "item": [
    {
      "name": "Health Check",
      "request": {
        "method": "GET",
        "header": [],
        "url": {
          "raw": "http://localhost:5000/api/health",
          "protocol": "http",
          "host": ["localhost"],
          "port": "5000",
          "path": ["api", "health"]
        }
      }
    },
    {
      "name": "Register",
      "request": {
        "method": "POST",
        "header": [
          {
            "key": "Content-Type",
            "value": "application/json"
          }
        ],
        "body": {
          "mode": "raw",
          "raw": "{\n  \"email\": \"user@example.com\",\n  \"username\": \"username\",\n  \"password\": \"Password123\",\n  \"full_name\": \"Nguyen Van A\",\n  \"phone\": \"0912345678\"\n}"
        },
        "url": {
          "raw": "http://localhost:5000/api/register",
          "protocol": "http",
          "host": ["localhost"],
          "port": "5000",
          "path": ["api", "register"]
        }
      }
    },
    {
      "name": "Login",
      "request": {
        "method": "POST",
        "header": [
          {
            "key": "Content-Type",
            "value": "application/json"
          }
        ],
        "body": {
          "mode": "raw",
          "raw": "{\n  \"login\": \"user@example.com\",\n  \"password\": \"Password123\"\n}"
        },
        "url": {
          "raw": "http://localhost:5000/api/login",
          "protocol": "http",
          "host": ["localhost"],
          "port": "5000",
          "path": ["api", "login"]
        }
      }
    }
  ]
}
```

---

## Database Schema

### Users Table
```sql
CREATE TABLE users (
    id VARCHAR(36) PRIMARY KEY,
    email VARCHAR(120) UNIQUE NOT NULL,
    username VARCHAR(80) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    full_name VARCHAR(120),
    phone VARCHAR(20),
    is_active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
```

### Password Reset Tokens Table
```sql
CREATE TABLE password_reset_tokens (
    id VARCHAR(36) PRIMARY KEY,
    user_id VARCHAR(36) NOT NULL,
    token VARCHAR(255) UNIQUE NOT NULL,
    expires_at TIMESTAMP NOT NULL,
    is_used BOOLEAN DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```

---

## Change Log

### v1.0.0 (January 2026)
- ✅ Health check endpoint
- ✅ User registration with validation
- ✅ User login with JWT
- ✅ Forgot password flow
- ✅ Reset password with token
- ✅ Get user profile (authenticated)
- ✅ CORS enabled
- ✅ Error handling
- ✅ Vietnamese error messages

---

**API Version:** 1.0.0  
**Last Updated:** January 12, 2026  
**Base URL:** http://localhost:5000/api  
**Documentation:** Complete
