import structlog

structlog.configure(
    processors=[
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.JSONRenderer()
    ]
)

logger = structlog.get_logger()

def validate_payment(amount):
    logger.info("Validating payment", amount=amount)
    if amount <= 0:
        logger.error("Invalid payment amount", amount=amount)
        raise ValueError("Invalid payment amount")
    return True

def process_order(user_id, amount):
    logger.info("Processing order", user_id=user_id)
    validate_payment(amount)
    total = amount * 1.2
    logger.info("Order processed", total=total)
    return total

def main():
    try:
        logger.info("Order system started")
        process_order(101, -50)
    except Exception as e:
        logger.error("Exception occurred", error=str(e))

if __name__ == "__main__":
    main()