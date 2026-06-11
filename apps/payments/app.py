from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"service": "payments"}

@app.get("/health")
def health():
    return {"status": "UP"}