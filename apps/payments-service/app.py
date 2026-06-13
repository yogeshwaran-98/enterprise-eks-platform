from fastapi import FastAPI

app = FastAPI()

payments = [
    {"id": 1, "amount": 100, "status": "success"},
    {"id": 2, "amount": 250, "status": "pending"}
]

@app.get("/")
def root():
    return {"service": "payments"}

@app.get("/payments")
def get_payments():
    return payments