from fastapi import FastAPI

from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.resources import Resource
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

app = FastAPI()

provider = TracerProvider(
     resource=Resource.create({
        "service.name": "users-service"
    })
)

provider.add_span_processor(
    BatchSpanProcessor(
        OTLPSpanExporter(
            endpoint="otel-collector-collector.observability.svc.cluster.local:4317",
            insecure=True,
        )
    )
)

trace.set_tracer_provider(provider)

FastAPIInstrumentor.instrument_app(app)

users = [
    {"id": 1, "name": "John"},
    {"id": 2, "name": "David"},
]

@app.get("/")
def root():
    return {"service": "users"}

@app.get("/users")
def get_users():
    return users