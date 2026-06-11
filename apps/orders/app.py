from fastapi import FastAPI

app = FastAPI()

orders = [
    {"id": 1, "product": "Laptop"},
    {"id": 2, "product": "Keyboard"}
]

@app.get("/")
def root():
    return {"service": "orders"}

@app.get("/orders")
def get_orders():
    return orders