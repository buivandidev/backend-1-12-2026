import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { Mail, ArrowLeft, Coffee, AlertCircle, CheckCircle } from 'lucide-react';
import { authAPI } from '../services/api';

const ForgotPassword = () => {
  const [email, setEmail] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [success, setSuccess] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    setSuccess(false);

    try {
      const response = await authAPI.forgotPassword(email);
      
      if (response.status === 'success') {
        setSuccess(true);
      }
    } catch (err) {
      setError(err.response?.data?.message || 'Đã xảy ra lỗi khi gửi email');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center p-4">
      <div className="w-full max-w-md">
        {/* Back to Login */}
        <Link 
          to="/login" 
          className="inline-flex items-center gap-2 text-amber-600 hover:text-amber-700 font-medium mb-8 transition-colors group"
        >
          <ArrowLeft className="w-5 h-5 group-hover:-translate-x-1 transition-transform" />
          Quay lại đăng nhập
        </Link>

        {/* Logo & Title */}
        <div className="text-center mb-8">
          <div className="inline-flex items-center justify-center w-16 h-16 bg-gradient-to-br from-amber-400 to-yellow-500 rounded-full mb-4 shadow-lg">
            <Coffee className="w-8 h-8 text-white" />
          </div>
          <h1 className="text-3xl font-bold text-gray-800 mb-2">
            Quên mật khẩu?
          </h1>
          <p className="text-gray-600">
            Nhập email của bạn để nhận link khôi phục mật khẩu
          </p>
        </div>

        {/* Forgot Password Card */}
        <div className="auth-card">
          {success ? (
            // Success Message
            <div className="text-center py-6">
              <div className="inline-flex items-center justify-center w-16 h-16 bg-green-100 rounded-full mb-4">
                <CheckCircle className="w-8 h-8 text-green-600" />
              </div>
              <h3 className="text-xl font-bold text-gray-800 mb-3">
                Email đã được gửi!
              </h3>
              <p className="text-gray-600 mb-6">
                Nếu email <span className="font-semibold text-amber-600">{email}</span> tồn tại trong hệ thống, bạn sẽ nhận được email hướng dẫn khôi phục mật khẩu trong vài phút.
              </p>
              <div className="bg-amber-50 border border-amber-200 rounded-lg p-4 mb-6">
                <p className="text-sm text-gray-700">
                  <span className="font-semibold">Lưu ý:</span> Vui lòng kiểm tra cả hộp thư spam nếu không thấy email trong hộp thư chính.
                </p>
              </div>
              <div className="space-y-3">
                <button
                  onClick={() => {
                    setSuccess(false);
                    setEmail('');
                  }}
                  className="btn-primary w-full"
                >
                  Gửi lại email
                </button>
                <Link to="/login" className="btn-secondary w-full inline-block text-center">
                  Quay lại đăng nhập
                </Link>
              </div>
            </div>
          ) : (
            // Forgot Password Form
            <>
              {/* Error Message */}
              {error && (
                <div className="mb-6 p-4 bg-red-50 border-l-4 border-red-500 text-red-700 rounded-lg flex items-start gap-3">
                  <AlertCircle className="w-5 h-5 mt-0.5 flex-shrink-0" />
                  <span className="text-sm">{error}</span>
                </div>
              )}

              {/* Info Message */}
              <div className="mb-6 p-4 bg-blue-50 border-l-4 border-blue-500 rounded-lg">
                <p className="text-sm text-blue-700">
                  Nhập địa chỉ email bạn đã đăng ký. Chúng tôi sẽ gửi link khôi phục mật khẩu đến email của bạn.
                </p>
              </div>

              <form onSubmit={handleSubmit} className="space-y-5">
                <div>
                  <label htmlFor="email" className="block text-sm font-semibold text-gray-700 mb-2">
                    Địa chỉ Email
                  </label>
                  <div className="relative">
                    <Mail className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400 w-5 h-5" />
                    <input
                      type="email"
                      id="email"
                      name="email"
                      value={email}
                      onChange={(e) => {
                        setEmail(e.target.value);
                        setError('');
                      }}
                      className="input-field pl-11"
                      placeholder="email@example.com"
                      required
                    />
                  </div>
                </div>

                <button
                  type="submit"
                  disabled={loading}
                  className="btn-primary w-full disabled:opacity-50 disabled:cursor-not-allowed"
                >
                  {loading ? (
                    <span className="flex items-center justify-center gap-2">
                      <svg className="animate-spin h-5 w-5" viewBox="0 0 24 24">
                        <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" fill="none"/>
                        <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"/>
                      </svg>
                      Đang gửi...
                    </span>
                  ) : (
                    'Gửi link khôi phục'
                  )}
                </button>
              </form>

              {/* Additional Help */}
              <div className="mt-6 pt-6 border-t border-gray-200">
                <p className="text-sm text-gray-600 text-center">
                  Gặp vấn đề khác?{' '}
                  <a href="#" className="text-amber-600 hover:text-amber-700 font-semibold hover:underline">
                    Liên hệ hỗ trợ
                  </a>
                </p>
              </div>
            </>
          )}
        </div>

        {/* Footer */}
        <p className="text-center text-sm text-gray-500 mt-8">
          © 2026 Drink Shop. All rights reserved.
        </p>
      </div>
    </div>
  );
};

export default ForgotPassword;
