# Drink Shop - Setup và Chạy Project

Write-Host "🍹 Drink Shop - Authentication System" -ForegroundColor Yellow
Write-Host "=====================================" -ForegroundColor Yellow
Write-Host ""

# Backend Setup
Write-Host "📦 Bước 1: Setup Backend (Flask API)" -ForegroundColor Cyan
Write-Host "------------------------------------" -ForegroundColor Cyan

$backendPath = "d:\backend1"
Set-Location $backendPath

# Kiểm tra virtual environment
if (!(Test-Path "venv")) {
    Write-Host "Tạo virtual environment..." -ForegroundColor Green
    python -m venv venv
}

Write-Host "Kích hoạt virtual environment..." -ForegroundColor Green
& ".\venv\Scripts\Activate.ps1"

Write-Host "Cài đặt Python dependencies..." -ForegroundColor Green
pip install -r requirements.txt

# Tạo .env nếu chưa có
if (!(Test-Path ".env")) {
    Write-Host "Tạo file .env từ .env.example..." -ForegroundColor Green
    Copy-Item .env.example .env
}

Write-Host ""
Write-Host "✅ Backend setup hoàn tất!" -ForegroundColor Green
Write-Host ""

# Frontend Setup
Write-Host "📦 Bước 2: Setup Frontend (React)" -ForegroundColor Cyan
Write-Host "------------------------------------" -ForegroundColor Cyan

$frontendPath = "d:\backend1\frontend"
Set-Location $frontendPath

if (!(Test-Path "node_modules")) {
    Write-Host "Cài đặt Node dependencies..." -ForegroundColor Green
    npm install
} else {
    Write-Host "Node modules đã được cài đặt." -ForegroundColor Yellow
}

Write-Host ""
Write-Host "✅ Frontend setup hoàn tất!" -ForegroundColor Green
Write-Host ""

# Hướng dẫn chạy
Write-Host "🚀 Hướng dẫn chạy ứng dụng:" -ForegroundColor Yellow
Write-Host "=====================================" -ForegroundColor Yellow
Write-Host ""
Write-Host "1️⃣  Chạy Backend (Terminal 1):" -ForegroundColor Cyan
Write-Host "   cd d:\backend1" -ForegroundColor White
Write-Host "   .\venv\Scripts\Activate.ps1" -ForegroundColor White
Write-Host "   python app.py" -ForegroundColor White
Write-Host "   👉 Backend sẽ chạy tại: http://localhost:5000" -ForegroundColor Green
Write-Host ""
Write-Host "2️⃣  Chạy Frontend (Terminal 2):" -ForegroundColor Cyan
Write-Host "   cd d:\backend1\frontend" -ForegroundColor White
Write-Host "   npm run dev" -ForegroundColor White
Write-Host "   👉 Frontend sẽ chạy tại: http://localhost:3000" -ForegroundColor Green
Write-Host ""
Write-Host "3️⃣  Mở trình duyệt và truy cập: http://localhost:3000" -ForegroundColor Cyan
Write-Host ""
Write-Host "✨ Chúc bạn phát triển vui vẻ!" -ForegroundColor Yellow
Write-Host ""
