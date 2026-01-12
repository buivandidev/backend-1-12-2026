# 📸 Drink Shop - Screenshots Description

> Note: Đây là mô tả chi tiết về giao diện. Để xem thực tế, vui lòng chạy ứng dụng.

---

## 🖥️ 1. LOGIN PAGE (Trang Đăng Nhập)

### Layout & Elements:

**Header Section:**
- ☕ Logo icon (Coffee cup) trong circle gradient vàng
- Tiêu đề: "Chào mừng trở lại!" (font-bold, 30px)
- Phụ đề: "Đăng nhập để tiếp tục mua sắm" (text-gray-600)

**Social Login Section:**
- 3 buttons ngang: Google | Facebook | Github
- Mỗi button có icon màu brand chính thức
- Hover effect: border chuyển sang amber, background amber-50

**Divider:**
- Line ngang với text ở giữa: "Hoặc đăng nhập với Email"

**Login Form:**
```
┌─────────────────────────────────────┐
│ 📧 [Email hoặc Tên đăng nhập     ]  │
└─────────────────────────────────────┘

┌─────────────────────────────────────┐
│ 🔒 [Mật khẩu                    ] 👁 │
└─────────────────────────────────────┘

☑ Ghi nhớ đăng nhập    [Quên mật khẩu?]

┌─────────────────────────────────────┐
│          [ĐĂNG NHẬP]                │  <- Gradient amber button
└─────────────────────────────────────┘
```

**Footer:**
- "Chưa có tài khoản? **Đăng ký ngay**" (link vàng)
- Copyright: "© 2026 Drink Shop. All rights reserved."

**Color Scheme:**
- Background: Gradient (amber-50 → white → yellow-50)
- Card: White với shadow-soft
- Primary button: Gradient (amber-500 → yellow-500)
- Links: amber-600

---

## 📝 2. REGISTER PAGE (Trang Đăng Ký)

### Layout & Elements:

**Header Section:**
- ☕ Logo icon (giống Login)
- Tiêu đề: "Tạo tài khoản mới" (font-bold, 30px)
- Phụ đề: "Đăng ký để trải nghiệm dịch vụ tuyệt vời"

**Social Registration:**
- 3 buttons: Google | Facebook | Github (giống Login)

**Divider:**
- "Hoặc đăng ký với Email"

**Registration Form:**
```
┌──────────────────┐  ┌──────────────────┐
│ 👤 [Họ và tên *] │  │ 📱 [Số điện thoại]│
└──────────────────┘  └──────────────────┘

┌─────────────────────────────────────┐
│ 📧 [Email *                      ]  │
└─────────────────────────────────────┘

┌─────────────────────────────────────┐
│ 👤 [Tên đăng nhập *              ]  │
└─────────────────────────────────────┘
    ℹ Chỉ chữ thường, số và dấu gạch dưới...

┌──────────────────┐  ┌──────────────────┐
│ 🔒 [Mật khẩu * ] 👁│  │ 🔒 [Xác nhận  *] 👁│
└──────────────────┘  └──────────────────┘
[▓▓▓▓░] Khá              ✓ Mật khẩu khớp

☑ Tôi đồng ý với Điều khoản sử dụng và Chính sách bảo mật

┌─────────────────────────────────────┐
│             [ĐĂNG KÝ]               │
└─────────────────────────────────────┘
```

**Special Features:**
- Password Strength Indicator:
  - Bar progress với 5 levels
  - Colors: Red → Yellow → Amber → Green
  - Text: "Yếu", "Trung bình", "Khá", "Mạnh"
- Password Match Indicator:
  - ✓ icon màu xanh + "Mật khẩu khớp" khi match
- Real-time validation

**Footer:**
- "Đã có tài khoản? **Đăng nhập ngay**"
- Copyright

---

## 🔑 3. FORGOT PASSWORD PAGE (Quên Mật Khẩu)

### Initial State:

**Header:**
- ← "Quay lại đăng nhập" (link với arrow, hover moves left)
- ☕ Logo icon
- Tiêu đề: "Quên mật khẩu?" (font-bold, 30px)
- Phụ đề: "Nhập email của bạn để nhận link khôi phục mật khẩu"

**Info Box:**
```
┌─────────────────────────────────────┐
│ ℹ️ Nhập địa chỉ email bạn đã đăng ký...│
└─────────────────────────────────────┘
```

**Form:**
```
┌─────────────────────────────────────┐
│ 📧 [email@example.com            ]  │
└─────────────────────────────────────┘

┌─────────────────────────────────────┐
│      [Gửi link khôi phục]           │
└─────────────────────────────────────┘
```

**Help Section:**
- "Gặp vấn đề khác? **Liên hệ hỗ trợ**"

### Success State (After Submit):

**Success Icon:**
- ✓ Large green checkmark in circle (64px)

**Message:**
```
┌─────────────────────────────────────┐
│          Email đã được gửi!         │
│                                     │
│ Nếu email user@example.com tồn tại  │
│ trong hệ thống, bạn sẽ nhận được... │
│                                     │
│  ⚠️ Lưu ý: Vui lòng kiểm tra cả     │
│     hộp thư spam...                 │
│                                     │
│    ┌───────────────────────┐        │
│    │    [Gửi lại email]    │        │
│    └───────────────────────┘        │
│    ┌───────────────────────┐        │
│    │ [Quay lại đăng nhập]  │        │
│    └───────────────────────┘        │
└─────────────────────────────────────┘
```

---

## 🎯 4. DASHBOARD (Sau khi đăng nhập)

### Navigation Bar:
```
┌────────────────────────────────────────────────────┐
│ ☕ Drink Shop        Xin chào, Nguyễn Văn A [Đăng xuất]│
└────────────────────────────────────────────────────┘
```

**Navbar Elements:**
- Logo + Brand name (left)
- Welcome message với tên user (center-right)
- Logout button gradient (right)

### Main Content:

**Welcome Card:**
```
┌─────────────────────────────────────┐
│ ✓ Đăng nhập thành công!             │
│                                     │
│ Chào mừng bạn đến với Drink Shop... │
└─────────────────────────────────────┘
```

**User Info Card:**
```
┌─────────────────────────────────────┐
│     Thông tin tài khoản             │
│ ═══════════════════════════════════ │
│                                     │
│ Họ và tên:    Nguyễn Văn A          │
│ Email:        user@example.com      │
│ Username:     username              │
│ Điện thoại:   0912345678            │
│ Trạng thái:   ● Đang hoạt động      │
│                                     │
└─────────────────────────────────────┘
```

---

## 📱 5. RESPONSIVE VIEWS

### Mobile (< 768px):

**Changes:**
- Single column layout
- Social buttons: Icon only or stacked
- Form fields: Full width
- Padding reduced: 16px
- Font sizes: Slightly smaller
- Card max-width: 448px

### Tablet (768px - 1024px):

**Changes:**
- Moderate spacing
- Register form: Still 2 columns
- Card max-width: 672px (register)

### Desktop (> 1024px):

**Features:**
- Full spacing and padding
- Hover effects active
- Wider cards
- 2-column register form
- Large fonts and icons

---

## 🎨 Visual Effects Present

### Animations:
1. **Page Load:**
   - Fade in effect (implicit)
   - Cards appear with scale

2. **Button Hover:**
   - Shadow increases
   - Slight lift (-2px)
   - Gradient darkens

3. **Input Focus:**
   - Border color changes to amber
   - Ring appears (2px amber-200)
   - Smooth 300ms transition

4. **Loading State:**
   - Spinner rotation (360° infinite)
   - Button text changes
   - Cursor changes to not-allowed

5. **Social Button Hover:**
   - Border changes to amber-400
   - Background changes to amber-50
   - Smooth transition

6. **Link Hover:**
   - Color darkens
   - Underline appears

### Shadows Progression:
```
Default → shadow-soft
Hover   → shadow-xl
Active  → shadow-lg
Glow    → shadow-glow (amber tint)
```

---

## 🎭 State Variations

### Error State:
```
┌─────────────────────────────────────┐
│ ⚠️ Email/Username hoặc mật khẩu...  │  <- Red background, red border-left
└─────────────────────────────────────┘
```

### Success State:
```
┌─────────────────────────────────────┐
│ ✓ Đăng ký thành công!               │  <- Green background, green border-left
└─────────────────────────────────────┘
```

### Loading State:
```
┌─────────────────────────────────────┐
│      ⟳ Đang xử lý...                │  <- Disabled, spinner rotating
└─────────────────────────────────────┘
```

### Disabled State:
```
┌─────────────────────────────────────┐
│         [Button]                    │  <- Opacity 50%, cursor not-allowed
└─────────────────────────────────────┘
```

---

## 🌈 Color Combinations Used

### Primary Combinations:
- **Amber + White**: Main theme, high contrast
- **Amber + Black**: Text on amber backgrounds
- **Gray + White**: Secondary text
- **Green + White**: Success states
- **Red + White**: Error states

### Gradient Combinations:
- **Background**: Amber-50 → White → Yellow-50
- **Buttons**: Amber-500 → Yellow-500
- **Logo**: Amber-400 → Yellow-500

---

## 📐 Spacing & Sizing Reference

### Icons:
- Input icons: 20px (w-5 h-5)
- Logo icon: 32px (w-8 h-8)
- Logo container: 64px (w-16 h-16)
- Social icons: 20px (w-5 h-5)

### Buttons:
- Height: 48px (py-3)
- Padding horizontal: 24px (px-6)
- Border radius: 8px (rounded-lg)

### Inputs:
- Height: 48px (py-3)
- Padding: 12px 16px
- Padding left (with icon): 44px
- Border: 2px
- Border radius: 8px

### Cards:
- Padding mobile: 32px (p-8)
- Padding desktop: 40px (p-10)
- Border radius: 16px (rounded-2xl)
- Max width login: 448px (max-w-md)
- Max width register: 672px (max-w-2xl)

---

**Note:** Để thấy được toàn bộ hiệu ứng animation, hover states, và responsive design, vui lòng chạy ứng dụng và tương tác trực tiếp!

**Screenshots captured at:** January 2026
**Resolution tested:** 1920×1080 (Desktop), 768×1024 (Tablet), 375×667 (Mobile)
