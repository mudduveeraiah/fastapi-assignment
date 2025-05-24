# 🛒 FastAPI Order Management API

A lightweight and fast **Order Management API** built using [FastAPI](https://fastapi.tiangolo.com/). This project enables users to manage customer orders with endpoints for creation, retrieval, updating, and summarization — all handled in memory for quick prototyping and testing.

---

## 📌 Features

This API supports basic operations needed for managing orders:

### ✅ Create Order
- Accepts a list of items and a total amount.
- Automatically assigns a unique ID and timestamps the order.
- Sets default status as `"pending"`.

### 📄 Retrieve All Orders
- Returns a list of all orders stored in memory.
- Useful for viewing the current order backlog.

### 🔍 Get Order by ID
- Fetches details for a single order using its unique ID.
- Returns a 404 error if the order does not exist.

### 🔄 Update Order Status
- Allows updating the `status` field of an existing order (e.g., from `"pending"` to `"completed"`).

### 📊 Order Summary
- Returns total number of orders and the total value of all orders.
- Great for quick business insights or analytics.

### 🧪 Auto-Generated Docs
- Interactive Swagger UI available at `/docs`.
- Redoc documentation available at `/redoc`.

---

## ⚙️ Technologies Used

- **FastAPI** – Modern and fast web framework
- **Pydantic** – Data validation and parsing
- **Uvicorn** – ASGI web server for FastAPI
- **UUID** – For unique and safe order IDs
- **Python datetime** – For order timestamps

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/mudduveeraiah/fastapi-assignment.git
cd fastapi-assignment
```

### 2. Install Dependencies

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install fastapi uvicorn
```

### 3. Run the Server

```bash
uvicorn main:app --reload
```

> Replace `main` with your actual filename if it's different (e.g., `app.py`, `api.py`).

---

✅ You're ready to go!

---
