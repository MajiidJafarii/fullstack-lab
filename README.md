# 🚀 Fullstack Lab

<p align="center">
یک پروژه فول‌استک مدرن با معماری مقیاس‌پذیر برای مدیریت کاربران، احراز هویت، داشبورد و سیستم بلاگ.
</p>

---

## 🧩 معرفی پروژه

**Fullstack Lab** یک پروژه فول‌استک واقعی با هدف پیاده‌سازی یک سیستم قابل توسعه و نزدیک به استانداردهای صنعتی است.

تمرکز اصلی پروژه:

- معماری تمیز و مقیاس‌پذیر
- جداسازی مسئولیت‌ها در Frontend و Backend
- احراز هویت امن کاربران
- مدیریت Session
- طراحی رابط کاربری مدرن
- ارتباط استاندارد بین Client و API

---

# ✨ امکانات

## 🔐 Authentication

- ثبت‌نام کاربران
- ورود کاربران
- مدیریت Session
- دریافت اطلاعات کاربر
- خروج از حساب
- تایید ایمیل با کد ۶ رقمی
- تغییر رمز عبور


## 📝 Blog System

- ایجاد پست
- ویرایش پست
- حذف پست
- مدیریت تصاویر پست
- نمایش لیست مطالب
- API مبتنی بر OpenAPI


## 🎨 رابط کاربری

- طراحی کامل RTL برای زبان فارسی
- پشتیبانی از Dark / Light Theme
- فونت Vazirmatn
- Sidebar واکنش‌گرا
- کامپوننت‌های قابل استفاده مجدد
- طراحی مدرن مبتنی بر shadcn/ui

---

# 🛠 تکنولوژی‌ها

## Frontend

| تکنولوژی | کاربرد |
|---|---|
| React | ساخت رابط کاربری |
| TypeScript | توسعه امن و قابل نگهداری |
| Vite | ابزار Build و Development |
| Tailwind CSS | طراحی UI |
| shadcn/ui | کامپوننت‌های رابط کاربری |
| React Router | مدیریت Routing |
| TanStack Query | مدیریت داده‌های Server |
| Axios | ارتباط HTTP |
| Orval | تولید خودکار API Client از OpenAPI |


## Backend

| تکنولوژی | کاربرد |
|---|---|
| Django | فریم‌ورک Backend |
| Django REST Framework | ساخت REST API |
| PostgreSQL | پایگاه داده |
| JWT Authentication | احراز هویت |


## DevOps

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
│
├── widgets
│
├── features
│
├── entities
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
- مناسب پروژه‌های بزرگ و تیمی

---

# 🚀 اجرای پروژه

## روش پیشنهادی: Docker


### Clone پروژه

```bash
git clone https://github.com/MajiidJafarii/fullstack-lab.git
```


### ورود به پروژه

```bash
cd fullstack-lab
```


### اجرای سرویس‌ها

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


اجرای Development:

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


نصب وابستگی‌ها:

```bash
pip install -r requirements.txt
```


Migration:

```bash
python manage.py migrate
```


اجرای سرور:

```bash
python manage.py runserver
```

---

# ⚙️ Environment Variables

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

پروژه دارای REST API استاندارد است.


نمونه Endpoint ها:


## Authentication

```
POST /api/auth/login/
```

```
POST /api/auth/register/
```

```
POST /api/auth/verify-email/
```


## User

```
GET /api/me/
```

```
POST /api/me/change-password/
```


## Blog

```
GET /api/blog/posts/
```

```
POST /api/blog/posts/
```

```
PATCH /api/blog/posts/{id}/
```

```
DELETE /api/blog/posts/{id}/
```

---

# 🧪 بررسی کیفیت پروژه


Frontend:

```bash
npm run fsd
npm run build
```


بررسی موارد:

- صحت TypeScript
- Production Build
- استاندارد معماری FSD

---

# 🗺 Roadmap آینده


- [ ] سیستم Role و Permission
- [ ] پنل مدیریت کاربران
- [ ] گزارش‌های پیشرفته
- [ ] تست کامل Backend
- [ ] تست کامل Frontend
- [ ] CI/CD با GitHub Actions
- [ ] اعلان‌ها
- [ ] Deployment روی سرور

---

# 👨‍💻 Author

**Majid Jafari**

Fullstack Developer
