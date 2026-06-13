from fastapi import FastAPI

from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider

app = FastAPI()

trace.set_tracer_provider(TracerProvider())

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