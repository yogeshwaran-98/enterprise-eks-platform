from fastapi import FastAPI

app = FastAPI()

inventory = [
    {"id": 1, "item": "Laptop", "stock": 10},
    {"id": 2, "item": "Mouse", "stock": 50}
]

@app.get("/")
def root():
    return {"service": "inventory"}

@app.get("/inventory")
def get_inventory():
    return inventory