# 🎨 Drink Shop - UI/UX Design Specifications

## 📐 Design Philosophy

Hệ thống Authentication của Drink Shop được thiết kế với triết lý **"Hiện đại, Sang trọng, Năng động"** - phản ánh tinh thần của một thương hiệu đồ uống cao cấp.

---

## 🎨 Color System

### Primary Colors (Amber/Yellow - Màu chủ đạo)

Amber được chọn làm màu chủ đạo vì:
- Tạo cảm giác **năng động, tươi trẻ**
- Gợi nhớ đến màu sắc của các loại đồ uống: trà, cà phê, nước ép
- Tạo điểm nhấn mạnh mẽ và thu hút

```css
Primary Amber Scale:
--amber-50:  #fffbeb  /* Background nhẹ nhàng */
--amber-100: #fef3c7  /* Hover states */
--amber-200: #fde68a
--amber-300: #fcd34d
--amber-400: #fbbf24  /* Light variant */
--amber-500: #f59e0b  /* 🌟 MAIN COLOR */
--amber-600: #d97706  /* Hover dark */
--amber-700: #b45309  /* Active states */
--amber-800: #92400e
--amber-900: #78350f
```

### Supporting Colors

**White (Trắng):**
- `#FFFFFF` - Background chính, cards
- `#F9FAFB` - Secondary background
- Tạo sự sạch sẽ, thoáng đãng

**Black/Gray (Đen/Xám):**
- `#000000` - Text chính (thường dùng #1F2937)
- `#6B7280` - Text phụ
- `#E5E7EB` - Borders
- Tạo độ tương phản, dễ đọc

**Status Colors:**
- Success: `#10B981` (Green)
- Error: `#EF4444` (Red)
- Warning: `#F59E0B` (Amber)
- Info: `#3B82F6` (Blue)

---

## 🔤 Typography

### Font Family
```css
font-family: 'Inter', system-ui, -apple-system, sans-serif;
```

**Lý do chọn Inter:**
- Modern, clean, professional
- Dễ đọc trên cả desktop và mobile
- Hỗ trợ nhiều font-weights

### Font Sizes & Weights

**Headings:**
- H1: `text-3xl` (30px) - Font Weight: 700 (Bold)
- H2: `text-2xl` (24px) - Font Weight: 700 (Bold)
- H3: `text-xl` (20px) - Font Weight: 600 (Semibold)

**Body Text:**
- Regular: `text-base` (16px) - Font Weight: 400 (Normal)
- Small: `text-sm` (14px) - Font Weight: 400 (Normal)
- Tiny: `text-xs` (12px) - Font Weight: 400 (Normal)

**Buttons & Labels:**
- Font Weight: 600 (Semibold)
- Letter Spacing: Normal

---

## 📦 Components Design

### 1. Cards (.auth-card)
```css
Properties:
- Background: White (#FFFFFF)
- Border Radius: 1rem (16px) - Bo góc mềm mại
- Shadow: shadow-soft (custom shadow nhẹ)
- Padding: 2rem (32px) on mobile, 2.5rem (40px) on desktop
- Hover: Shadow tăng lên (shadow-xl)
- Transition: 300ms ease
```

**Design Intent:**
- Tạo sự nổi bật trên background gradient
- Shadow nhẹ tạo depth tinh tế
- Hover effect để tăng tính tương tác

### 2. Buttons

**Primary Button (.btn-primary)**
```css
Properties:
- Background: Linear gradient (amber-500 → yellow-500)
- Text Color: White
- Padding: 0.75rem 1.5rem (12px 24px)
- Border Radius: 0.5rem (8px)
- Shadow: Medium shadow with amber tint
- Hover: Gradient darker + Shadow increase + Lift -2px
- Transition: All 300ms
- Font Weight: 600 (Semibold)
```

**Secondary Button (.btn-secondary)**
```css
Properties:
- Background: Transparent
- Border: 2px solid amber-500
- Text Color: amber-700
- Hover: Background amber-50
- Same padding and border-radius as primary
```

**Social Button (.social-btn)**
```css
Properties:
- Background: White
- Border: 2px solid gray-300
- Hover Border: amber-400
- Hover Background: amber-50
- Display: Flex with icon gap
- Square-ish with icon-only or icon+text
```

### 3. Input Fields (.input-field)
```css
Properties:
- Border: 2px solid gray-200
- Border Radius: 0.5rem (8px)
- Padding: 0.75rem 1rem (12px 16px)
- Padding Left: 2.75rem (44px) - For icons
- Focus Border: amber-500
- Focus Ring: 2px ring amber-200
- Transition: All 300ms
- Background: White
```

**Icons in Input:**
- Position: Absolute left
- Color: gray-400
- Size: 20px (w-5 h-5)
- Y-Center: Transform translateY(-50%)

### 4. Logo/Brand Icon
```css
Properties:
- Shape: Circle (rounded-full) or rounded square
- Size: 64px × 64px (w-16 h-16)
- Background: Gradient (amber-400 → yellow-500)
- Icon: Coffee cup (w-8 h-8)
- Icon Color: White
- Shadow: Large shadow
```

---

## 🎭 Visual Effects

### Shadows
```css
/* Soft Shadow - Cho cards */
shadow-soft: 0 2px 15px -3px rgba(0, 0, 0, 0.07), 
             0 10px 20px -2px rgba(0, 0, 0, 0.04)

/* Glow Effect - Cho buttons hover */
shadow-glow: 0 0 20px rgba(245, 158, 11, 0.3)

/* Medium Shadow */
shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1)

/* Large Shadow */
shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1)

/* Extra Large Shadow - Hover states */
shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.1)
```

### Animations & Transitions

**Standard Transition:**
```css
transition: all 300ms ease-in-out
```

**Hover Effects:**
- Buttons: Scale subtle + Shadow increase + Y-translate -2px
- Cards: Shadow increase from soft to xl
- Links: Color change + Underline
- Social buttons: Border color + Background color

**Loading Spinner:**
- SVG circle animation
- Spin 1 full rotation
- Duration: 1s
- Timing: Linear
- Infinite loop

### Gradients

**Background Gradient:**
```css
background: linear-gradient(to bottom right, 
  #fffbeb,  /* amber-50 */
  #ffffff,  /* white */
  #fefce8   /* yellow-50 */
)
```

**Button Gradient:**
```css
background: linear-gradient(to right,
  #f59e0b,  /* amber-500 */
  #eab308   /* yellow-500 */
)
```

**Logo Gradient:**
```css
background: linear-gradient(to bottom right,
  #fbbf24,  /* amber-400 */
  #eab308   /* yellow-500 */
)
```

---

## 📱 Responsive Design

### Breakpoints (Tailwind defaults)
```css
sm:  640px   /* Small tablets */
md:  768px   /* Tablets */
lg:  1024px  /* Small laptops */
xl:  1280px  /* Desktops */
2xl: 1536px  /* Large screens */
```

### Mobile-First Approach

**Mobile (< 768px):**
- Single column layout
- Full width cards (max-w-md)
- Padding: 1rem
- Font sizes: Slightly smaller
- Social buttons: Icon only or stacked

**Desktop (≥ 768px):**
- Wider cards (max-w-2xl for register)
- Two-column forms
- Padding: 2.5rem
- Larger fonts and spacing

**Key Responsive Classes:**
```jsx
// Container
"max-w-md"              // Mobile: 448px max
"md:max-w-2xl"          // Desktop: 672px for register

// Grid
"grid-cols-1"           // Mobile: 1 column
"md:grid-cols-2"        // Desktop: 2 columns

// Padding
"p-4"                   // Mobile: 16px
"md:p-10"               // Desktop: 40px

// Text
"text-3xl"              // Mobile: 30px
"md:text-4xl"           // Desktop: 36px
```

---

## 🎯 User Experience Patterns

### 1. **Visual Feedback**
- Hover states trên tất cả interactive elements
- Loading states với spinner animation
- Success/Error messages với icons và colors phù hợp
- Disabled states với opacity giảm

### 2. **Progressive Disclosure**
- Password visibility toggle
- Error messages chỉ hiện khi có lỗi
- Success messages thay thế form sau khi submit

### 3. **Micro-interactions**
- Button hover: Lift effect (-2px translate)
- Input focus: Ring animation
- Link hover: Color change + underline
- Social button hover: Background + border color

### 4. **Accessibility**
- Proper label associations
- Required field indicators (*)
- Error messages with aria attributes
- Keyboard navigation support
- Focus visible states
- Sufficient color contrast (WCAG AA)

### 5. **Validation Feedback**
- Real-time password strength indicator
- Confirm password match indicator
- Field-level error messages
- Icon indicators (checkmark for success)

---

## 🖼️ Layout Structure

### Page Layout
```
┌─────────────────────────────────────┐
│         Background Gradient         │
│  ┌───────────────────────────────┐  │
│  │         Logo + Title          │  │
│  └───────────────────────────────┘  │
│  ┌───────────────────────────────┐  │
│  │                               │  │
│  │        Auth Card              │  │
│  │    (Login/Register/Forgot)    │  │
│  │                               │  │
│  └───────────────────────────────┘  │
│  ┌───────────────────────────────┐  │
│  │       Footer Text             │  │
│  └───────────────────────────────┘  │
└─────────────────────────────────────┘
```

### Card Internal Structure
```
┌─────────────────────────────────┐
│     Social Login Buttons        │  (3 buttons: Google, FB, Github)
├─────────────────────────────────┤
│          Divider                │  ("Hoặc đăng nhập với Email")
├─────────────────────────────────┤
│                                 │
│      Form Fields                │  (Inputs with icons)
│                                 │
├─────────────────────────────────┤
│    Additional Options           │  (Remember me, Forgot password)
├─────────────────────────────────┤
│     Submit Button               │  (Primary button)
├─────────────────────────────────┤
│     Alternative Action          │  (Link to Register/Login)
└─────────────────────────────────┘
```

---

## 🎨 Icon Usage (Lucide React)

### Icons per Component

**Login:**
- `Coffee` - Logo/Brand
- `Mail` - Email input
- `Lock` - Password input
- `Eye` / `EyeOff` - Password visibility toggle
- `AlertCircle` - Error messages
- Social icons: SVG paths (Google, Facebook, Github)

**Register:**
- `Coffee` - Logo/Brand
- `User` - Username & Full name input
- `Mail` - Email input
- `Phone` - Phone input
- `Lock` - Password inputs
- `Eye` / `EyeOff` - Password visibility
- `CheckCircle2` - Password match indicator
- `AlertCircle` - Error messages

**Forgot Password:**
- `Coffee` - Logo/Brand
- `Mail` - Email input
- `ArrowLeft` - Back to login
- `CheckCircle` - Success state
- `AlertCircle` - Error messages

**Dashboard:**
- `Coffee` - Logo
- `CheckCircle2` - Success message

---

## 📊 Design Metrics

### Spacing Scale (Tailwind)
```
0.5 → 2px
1   → 4px
2   → 8px
3   → 12px
4   → 16px
5   → 20px
6   → 24px
8   → 32px
10  → 40px
12  → 48px
```

### Common Spacings Used
- Card padding: `p-8` (32px) mobile, `md:p-10` (40px) desktop
- Form field gaps: `space-y-5` (20px)
- Button padding: `py-3 px-6` (12px 24px)
- Icon sizes: `w-5 h-5` (20px) for inputs, `w-8 h-8` (32px) for logo

---

## ✨ Special Features

### Password Strength Indicator
```jsx
Visual: Horizontal bar with 5 segments
Colors by strength:
- 0-2 segments: Red (Yếu)
- 3 segments: Yellow (Trung bình)
- 4 segments: Amber (Khá)
- 5 segments: Green (Mạnh)

Animation: Width transition 300ms
```

### Social Login Buttons
```jsx
Layout: Grid 3 columns
Icons: Official brand colors
  - Google: Multi-color (Blue, Red, Yellow, Green)
  - Facebook: #1877F2 (Blue)
  - Github: #181717 (Black)
Size: 20px × 20px icons
Border: 2px gray-300, hover: amber-400
```

### Loading States
```jsx
Component: Inline spinner + text
Position: Replace button text
Animation: Rotate 360° infinite
Color: Inherit from button (white)
Size: 20px × 20px
```

---

## 🎯 Design Goals Achieved

✅ **Modern & Clean** - Minimalist design với focus vào nội dung
✅ **Professional** - Color scheme và typography chuyên nghiệp
✅ **Energetic** - Amber color tạo cảm giác năng động
✅ **User-friendly** - Clear labels, helpful hints, instant feedback
✅ **Accessible** - Proper contrast, focus states, semantic HTML
✅ **Responsive** - Hoạt động tốt trên mọi devices
✅ **Consistent** - Reusable components, unified design system
✅ **Engaging** - Smooth animations, hover effects, micro-interactions

---

**Design System Version:** 1.0
**Last Updated:** January 2026
**Designer:** Senior Full-stack Developer Team
