import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

def validate_payment(amount):
    logger.info("Validating payment")
    if amount <= 0:
        logger.error("Invalid payment amount")
        raise ValueError("Invalid payment amount")
    return True

def process_order(user_id, amount):
    logger.info(f"Processing order for user {user_id}")
    validate_payment(amount)
    total = amount * 1.2
    logger.info(f"Order processed with total {total}")
    return total

def main():
    try:
        logger.info("Order system started")
        process_order(101, -50)
    except Exception as e:
        logger.exception("Exception occurred")

if __name__ == "__main__":
    main()