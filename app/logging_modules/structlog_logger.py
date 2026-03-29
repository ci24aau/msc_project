import structlog

# Configure structlog for JSON structured logs
structlog.configure(
    processors=[
        structlog.processors.JSONRenderer()
    ]
)

logger = structlog.get_logger()