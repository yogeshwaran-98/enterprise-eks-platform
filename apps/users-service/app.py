from fastapi import FastAPI

app = FastAPI()

users = [
    {"id": 1, "name": "John"},
    {"id": 2, "name": "David"}
]

@app.get("/")
def root():
    return {"service": "users"}

@app.get("/users")
def get_users():
    return users