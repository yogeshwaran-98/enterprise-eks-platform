from fastapi import FastAPI

app = FastAPI()

orders = [
    {"id": 1, "item": "Laptop", "quantity": 1},
    {"id": 2, "item": "Phone", "quantity": 2}
]

@app.get("/")
def root():
    return {"service": "orders"}

@app.get("/orders")
def get_orders():
    return orders