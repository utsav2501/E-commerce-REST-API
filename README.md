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
git clone https://github.com/yourusername/ecommerce-api.git
cd ecommerce-api
