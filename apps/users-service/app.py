from fastapi import FastAPI

from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider

app = FastAPI()

trace.set_tracer_provider(TracerProvider())
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