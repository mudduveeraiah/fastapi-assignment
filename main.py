from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel
from typing import List
from uuid import uuid4
from datetime import datetime

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Order API is running. Visit /docs for API documentation."}

# Order data models
class OrderCreate(BaseModel):
    items: List[str]
    total: float

class OrderUpdate(BaseModel):
    status: str

class Order(BaseModel):
    id: str
    items: List[str]
    total: float
    status: str
    created_at: datetime

class OrderSummary(BaseModel):
    total_orders: int
    total_value: float

# In-memory order storage
orders = {}

# Create new order
@app.post("/orders", response_model=Order)
def create_order(order_data: OrderCreate):
    order_id = str(uuid4())
    new_order = Order(
        id=order_id,
        items=order_data.items,
        total=order_data.total,
        status="pending",
        created_at=datetime.utcnow()
    )
    orders[order_id] = new_order
    return new_order

# Get all orders
@app.get("/orders", response_model=List[Order])
def get_all_orders():
    return list(orders.values())

# ✅ Move summary route BEFORE /orders/{order_id}
@app.get("/orders/summary", response_model=OrderSummary)
def get_summary():
    total_orders = len(orders)
    total_value = sum(order.total for order in orders.values())
    return OrderSummary(total_orders=total_orders, total_value=total_value)

# Get a single order by ID
@app.get("/orders/{order_id}", response_model=Order)
def get_order(order_id: str):
    if order_id not in orders:
        raise HTTPException(status_code=404, detail="Order not found")
    return orders[order_id]

# Update the status of an order
@app.put("/orders/{order_id}", response_model=Order)
def update_order(order_id: str, update_data: OrderUpdate):
    if order_id not in orders:
        raise HTTPException(status_code=404, detail="Order not found")
    orders[order_id].status = update_data.status
    return orders[order_id]
