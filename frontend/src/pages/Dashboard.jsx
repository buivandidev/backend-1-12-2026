import React from 'react';
import { Coffee, CheckCircle } from 'lucide-react';

const Dashboard = () => {
  const user = JSON.parse(localStorage.getItem('user') || '{}');

  const handleLogout = () => {
    localStorage.removeItem('access_token');
    localStorage.removeItem('user');
    window.location.href = '/login';
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-amber-50 via-white to-yellow-50">
      {/* Navigation Bar */}
      <nav className="bg-white shadow-md border-b-2 border-amber-400">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center h-16">
            <div className="flex items-center gap-3">
              <div className="flex items-center justify-center w-10 h-10 bg-gradient-to-br from-amber-400 to-yellow-500 rounded-lg shadow">
                <Coffee className="w-6 h-6 text-white" />
              </div>
              <span className="text-xl font-bold text-gray-800">Drink Shop</span>
            </div>
            <div className="flex items-center gap-4">
              <span className="text-gray-700 font-medium">
                Xin chào, <span className="text-amber-600">{user.full_name}</span>
              </span>
              <button
                onClick={handleLogout}
                className="px-4 py-2 text-sm font-medium text-white bg-gradient-to-r from-amber-500 to-yellow-500 hover:from-amber-600 hover:to-yellow-600 rounded-lg transition-all duration-300 shadow-md hover:shadow-lg"
              >
                Đăng xuất
              </button>
            </div>
          </div>
        </div>
      </nav>

      {/* Main Content */}
      <div className="max-w-4xl mx-auto px-4 py-12">
        {/* Welcome Card */}
        <div className="bg-white rounded-2xl shadow-soft p-8 mb-8">
          <div className="flex items-center gap-3 mb-4">
            <CheckCircle className="w-8 h-8 text-green-500" />
            <h1 className="text-3xl font-bold text-gray-800">
              Đăng nhập thành công!
            </h1>
          </div>
          <p className="text-gray-600 text-lg">
            Chào mừng bạn đến với Drink Shop. Hệ thống xác thực đã hoạt động hoàn hảo!
          </p>
        </div>

        {/* User Info Card */}
        <div className="bg-white rounded-2xl shadow-soft p-8">
          <h2 className="text-2xl font-bold text-gray-800 mb-6 pb-4 border-b-2 border-amber-400">
            Thông tin tài khoản
          </h2>
          <div className="space-y-4">
            <div className="flex items-start gap-4">
              <div className="w-32 font-semibold text-gray-700">Họ và tên:</div>
              <div className="flex-1 text-gray-900">{user.full_name || 'N/A'}</div>
            </div>
            <div className="flex items-start gap-4">
              <div className="w-32 font-semibold text-gray-700">Email:</div>
              <div className="flex-1 text-gray-900">{user.email || 'N/A'}</div>
            </div>
            <div className="flex items-start gap-4">
              <div className="w-32 font-semibold text-gray-700">Username:</div>
              <div className="flex-1 text-gray-900">{user.username || 'N/A'}</div>
            </div>
            <div className="flex items-start gap-4">
              <div className="w-32 font-semibold text-gray-700">Điện thoại:</div>
              <div className="flex-1 text-gray-900">{user.phone || 'Chưa cập nhật'}</div>
            </div>
            <div className="flex items-start gap-4">
              <div className="w-32 font-semibold text-gray-700">Trạng thái:</div>
              <div className="flex-1">
                <span className="inline-flex items-center gap-2 px-3 py-1 bg-green-100 text-green-700 rounded-full text-sm font-medium">
                  <span className="w-2 h-2 bg-green-500 rounded-full"></span>
                  Đang hoạt động
                </span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
