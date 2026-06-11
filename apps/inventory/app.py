from fastapi import FastAPI

app = FastAPI()

inventory = [
    {"item": "Laptop", "stock": 20},
    {"item": "Keyboard", "stock": 50}
]

@app.get("/")
def root():
    return {"service": "inventory"}

@app.get("/inventory")
def get_inventory():
    return inventory