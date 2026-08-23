# 🚀 Fullstack Lab

<p align="center">

یک پروژه فول‌استک مدرن با معماری حرفه‌ای برای مدیریت کاربران، احراز هویت، داشبورد و تنظیمات حساب کاربری.

</p>


---

# 🧩 معرفی پروژه

**Fullstack Lab** یک سامانه فول‌استک مدرن است که با هدف پیاده‌سازی یک پروژه واقعی، قابل توسعه و نزدیک به استانداردهای صنعتی ساخته شده است.

تمرکز اصلی پروژه:

- معماری تمیز و قابل توسعه
- ارتباط استاندارد بین Frontend و Backend
- احراز هویت امن کاربران
- مدیریت Session
- طراحی رابط کاربری مدرن
- استفاده از ابزارهای روز توسعه نرم‌افزار


---

# ✨ امکانات پروژه


## 🔐 سیستم احراز هویت

- ثبت‌نام کاربران
- ورود کاربران
- مدیریت Session
- دریافت اطلاعات کاربر
- خروج از حساب
- تایید ایمیل با کد ۶ رقمی
- تغییر رمز عبور


## 🎨 رابط کاربری

- طراحی کاملاً RTL برای زبان فارسی
- پشتیبانی از حالت روشن و تاریک
- فونت Vazirmatn
- Sidebar واکنش‌گرا
- طراحی صفحات مدیریتی
- کامپوننت‌های قابل استفاده مجدد


## 📊 صفحات سیستم

- صفحه اصلی
- داشبورد مدیریتی
- پروفایل کاربر
- تنظیمات حساب
- تغییر رمز عبور


---

# 🛠 تکنولوژی‌های استفاده شده


# Frontend

| تکنولوژی | کاربرد |
|---|---|
| React | ساخت رابط کاربری |
| TypeScript | توسعه امن و قابل نگهداری |
| Vite | ابزار توسعه و Build |
| Tailwind CSS | طراحی رابط کاربری |
| shadcn/ui | کامپوننت‌های UI |
| React Router | مدیریت مسیرها |
| TanStack Query | مدیریت درخواست‌های API |
| Axios | ارتباط HTTP |
| Orval | تولید خودکار API Client از OpenAPI |


# Backend

| تکنولوژی | کاربرد |
|---|---|
| Django | فریم‌ورک اصلی Backend |
| Django REST Framework | ساخت API |
| PostgreSQL | دیتابیس |
| JWT Authentication | احراز هویت مبتنی بر Token |


# DevOps

| تکنولوژی | کاربرد |
|---|---|
| Docker | کانتینرسازی |
| Docker Compose | مدیریت سرویس‌ها |


---

# 🏗 معماری پروژه


## Frontend Architecture

ساختار Frontend بر اساس:

```
Feature-Sliced Design (FSD)
```

پیاده‌سازی شده است.


ساختار کلی:

```
src
│
├── app
│   ├── providers
│   ├── routing
│   └── layout
│
├── pages
│   ├── home
│   ├── dashboard
│   └── settings
│
├── widgets
│   ├── header
│   └── sidebar
│
├── features
│   ├── auth-login
│   ├── auth-register
│   ├── change-password
│   └── theme-toggle
│
├── entities
│   ├── user
│   └── session
│
└── shared
    ├── ui
    ├── api
    └── lib
```


مزایای این معماری:

- جلوگیری از پیچیدگی پروژه
- جداسازی مسئولیت‌ها
- توسعه آسان قابلیت‌های جدید
- مناسب برای پروژه‌های بزرگ


---

# 🚀 اجرای پروژه


## روش اول: Docker (پیشنهادی)


### دریافت پروژه

```bash
git clone https://github.com/MajiidJafarii/fullstack-lab.git
```


ورود به پروژه:

```bash
cd fullstack-lab
```


اجرای پروژه:

```bash
docker compose up --build
```


بعد از اجرا:


Frontend:

```
http://localhost:5173
```


Backend:

```
http://localhost:8000
```


---

# اجرای Frontend به صورت جداگانه


ورود:

```bash
cd frontend
```


نصب وابستگی‌ها:

```bash
npm install
```


اجرای پروژه:

```bash
npm run dev
```


Build:

```bash
npm run build
```


بررسی معماری FSD:

```bash
npm run fsd
```


---

# اجرای Backend به صورت جداگانه


ورود:

```bash
cd backend
```


ساخت محیط مجازی:

```bash
python -m venv .venv
```


فعال‌سازی محیط مجازی:

Linux / macOS:

```bash
source .venv/bin/activate
```


Windows:

```bash
.venv\Scripts\activate
```


نصب وابستگی‌ها:

```bash
pip install -r requirements.txt
```


اجرای Migration:

```bash
python manage.py migrate
```


اجرای سرور:

```bash
python manage.py runserver
```


---

# ⚙️ متغیرهای محیطی


قبل از اجرا فایل:

```
.env
```

ایجاد کنید.


نمونه:

```env
DEBUG=True

DATABASE_NAME=postgres

DATABASE_USER=postgres

DATABASE_PASSWORD=password

DATABASE_HOST=db

DATABASE_PORT=5432
```


---

# 🔌 API


پروژه دارای API مبتنی بر REST است.


نمونه Endpoint ها:


## ورود

```
POST /api/auth/login/
```


## ثبت‌نام

```
POST /api/auth/register/
```


## تایید ایمیل

```
POST /api/auth/verify-email/
```


## تغییر رمز

```
POST /api/me/change-password/
```


---

# 🧪 بررسی کیفیت پروژه


Frontend:

```bash
npm run fsd

npm run build
```


این دستورات بررسی می‌کنند:

- صحت TypeScript
- ساخت Production
- استاندارد بودن معماری FSD


---

# 🗺 مسیر توسعه آینده


- [ ] سیستم نقش‌ها و سطح دسترسی کاربران
- [ ] پنل مدیریت کاربران
- [ ] گزارش‌های پیشرفته
- [ ] تست‌های کامل Backend
- [ ] تست‌های کامل Frontend
- [ ] CI/CD با GitHub Actions
- [ ] اعلان‌ها
- [ ] استقرار روی سرور

