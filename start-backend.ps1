# Start Backend Server
Write-Host "🚀 Starting Backend Server (Flask)..." -ForegroundColor Cyan

Set-Location "d:\backend1"

# Kích hoạt virtual environment
& ".\venv\Scripts\Activate.ps1"

# Chạy Flask server
Write-Host "Backend server đang chạy tại: http://localhost:5000" -ForegroundColor Green
python app.py
