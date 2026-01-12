# 🚀 Hướng dẫn chạy nhanh - Drink Shop Authentication

## Cách 1: Sử dụng Script tự động (Khuyến nghị)

### Setup lần đầu:
```powershell
cd d:\backend1
.\setup.ps1
```

### Chạy ứng dụng:

**Terminal 1 - Backend:**
```powershell
cd d:\backend1
.\start-backend.ps1
```

**Terminal 2 - Frontend:**
```powershell
cd d:\backend1
.\start-frontend.ps1
```

---

## Cách 2: Chạy thủ công

### Backend (Flask)
```powershell
# Di chuyển vào thư mục backend
cd d:\backend1

# Tạo virtual environment (chỉ lần đầu)
python -m venv venv

# Kích hoạt virtual environment
.\venv\Scripts\Activate.ps1

# Cài đặt dependencies (chỉ lần đầu)
pip install -r requirements.txt

# Tạo file .env (chỉ lần đầu)
Copy-Item .env.example .env

# Chạy server
python app.py
```

### Frontend (React)
```powershell
# Di chuyển vào thư mục frontend
cd d:\backend1\frontend

# Cài đặt dependencies (chỉ lần đầu)
npm install

# Chạy development server
npm run dev
```

---

## 🌐 Truy cập

- **Frontend:** http://localhost:3000
- **Backend API:** http://localhost:5000
- **API Health Check:** http://localhost:5000/api/health

---

## 🧪 Test tài khoản

Sau khi đăng ký, bạn có thể sử dụng:
- **Email/Username:** (tài khoản bạn vừa tạo)
- **Password:** (mật khẩu bạn vừa đặt)

---

## 🔍 Kiểm tra API

### Sử dụng curl:
```powershell
# Health check
curl http://localhost:5000/api/health

# Register
curl -X POST http://localhost:5000/api/register `
  -H "Content-Type: application/json" `
  -d '{"email":"test@example.com","username":"testuser","password":"Password123","full_name":"Test User"}'

# Login
curl -X POST http://localhost:5000/api/login `
  -H "Content-Type: application/json" `
  -d '{"login":"test@example.com","password":"Password123"}'
```

---

## ⚠️ Lưu ý

1. Đảm bảo cả 2 servers (Backend và Frontend) đang chạy
2. Backend phải chạy trước Frontend
3. Port 5000 và 3000 phải available
4. Cần cài đặt Python 3.8+ và Node.js 16+

---

## 🐛 Gặp lỗi?

### Backend không khởi động:
- Kiểm tra Python đã cài đặt: `python --version`
- Kiểm tra virtual environment đã active: `Get-Command python`
- Xem log chi tiết trong terminal

### Frontend không khởi động:
- Kiểm tra Node.js đã cài đặt: `node --version`
- Xóa node_modules và cài lại: `rm -r node_modules; npm install`
- Clear cache: `npm cache clean --force`

### Lỗi CORS:
- Đảm bảo Backend đang chạy
- Kiểm tra URL API trong frontend/src/services/api.js

---

**Happy Coding! 🎉**
