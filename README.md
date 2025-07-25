# E-commerce-REST-API

A Django REST Framework-based e-commerce API that supports:
- User Registration & JWT Authentication
- Product & Category Management
- Cart & Order System with stock control
- Redis Caching for product/category optimization
- Real-time order status updates using Django Channels (WebSockets)

---

## 🚀 Features

- JWT-based authentication (SimpleJWT)
- PostgreSQL database
- Redis for caching
- Real-time order status notifications (Django Channels + Redis)
- Admin Panel to manage products, categories, and orders
- Pagination and filtering on product listings

---

## 🧰 Tech Stack

- **Backend**: Django, Django REST Framework
- **Database**: PostgreSQL
- **Authentication**: JWT (SimpleJWT)
- **Cache**: Redis
- **WebSockets**: Django Channels + Channels Redis

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/utsav2501/E-commerce-REST-API.git
cd ecommerce
```

### 2. Create & Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```
### 3. Install Dependencies

```bash
pip install -r requirements.txt
```
### 4. PostgreSQL Setup
Ensure PostgreSQL is running and create a database:
Update your ecommerce/settings.py:
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_pg_user',
        'PASSWORD': 'your_pg_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
### 5. Run Migrations & Create Superuser

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```
### 6. Run Development Server

```bash
pyhton manage.py runserver
```
## 🔐 Authentication
Use the following endpoints to obtain JWT tokens:

- POST /api/register/ – Register user

- POST /api/token/ – Get access & refresh token

- POST /api/token/refresh/ – Refresh token

## 📚 API Endpoints Summary
Users
- POST /api/register/

- GET /api/profile/ (auth required)

- PUT /api/profile/ (auth required)

Categories
- POST /api/categories/ (admin only)

- GET /api/shop/categories/ (public)

- POST/PUT/DELETE /api/categories/< id >/ (admin)

Products
- GET /api/products/ (admin only)

- GET /api/shop/products/ (public with filters)

- POST/PUT/DELETE /api/products/< id >/ (admin)

Orders
- POST /api/orders/ (auth required)

- GET /api/orders/history/ (auth required)

- PUT /api/orders/< id >/ (admin only, for status updates)
## ✅ Filtering Products
Example:

```bash
GET /api/shop/products/?category=1&stock=1
```
