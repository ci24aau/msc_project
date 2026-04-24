from fastapi import FastAPI, HTTPException
import uuid

from app.models import User, Order
from app.services import create_user, process_order

# ----------------------------
# CHANGE THIS TO SWITCH LOGGER
# ----------------------------
LOGGING_TYPE = "standard"   # options: standard, loguru, structlog


# ----------------------------
# IMPORT LOGGER BASED ON TYPE
# ----------------------------
if LOGGING_TYPE == "standard":
    from app.logging_modules.standard_logger import logger

elif LOGGING_TYPE == "loguru":
    from app.logging_modules.loguru_logger import logger

else:
    from app.logging_modules.structlog_logger import logger


app = FastAPI()


# ----------------------------
# HOME ENDPOINT
# ----------------------------
@app.get("/")
def home():
    return {"message": "E-commerce Logging System Running"}


# ----------------------------
# CREATE USER
# ----------------------------
@app.post("/create-user")
def create_user_api(user: User):

    # generate unique request ID
    request_id = str(uuid.uuid4())

    logger.info(f"Request {request_id}: Creating user")

    try:
        result = create_user(user)

        logger.info(f"Request {request_id}: User created successfully")

        return result

    except Exception as e:
        logger.exception(f"Request {request_id}: Error creating user")

        # ✅ FIX: return proper HTTP error
        raise HTTPException(
            status_code=500,
            detail=f"User creation failed: {str(e)}"
        )


# ----------------------------
# PROCESS ORDER
# ----------------------------
@app.post("/process-order")
def process_order_api(order: Order):

    request_id = str(uuid.uuid4())

    logger.info(f"Request {request_id}: Processing order")

    try:
        result = process_order(order)

        logger.info(f"Request {request_id}: Order completed")

        return result

    except Exception as e:
        logger.exception(f"Request {request_id}: Order failed")

        # ✅ FIX: return proper HTTP error
        raise HTTPException(
            status_code=500,
            detail=f"Order processing failed: {str(e)}"
        )


# ----------------------------
# CONTROLLED ERROR (RUNTIME)
# ----------------------------
@app.get("/trigger-error")
def trigger_error():

    request_id = str(uuid.uuid4())

    logger.info(f"Request {request_id}: Triggering runtime error")

    try:
        x = 10 / 0  # division by zero

    except Exception:
        logger.exception(f"Request {request_id}: Runtime error occurred")

        # ✅ FIX: proper error response
        raise HTTPException(
            status_code=500,
            detail="Runtime error occurred (division by zero)"
        )


# ----------------------------
# SYNTAX-LIKE ERROR
# ----------------------------
@app.get("/syntax-error")
def syntax_error():

    request_id = str(uuid.uuid4())

    logger.info(f"Request {request_id}: Simulating syntax error")

    try:
        eval("5 + * 2")  # invalid Python syntax

    except Exception:
        logger.exception(f"Request {request_id}: Syntax error occurred")

        # ✅ FIX: proper error response
        raise HTTPException(
            status_code=500,
            detail="Syntax error occurred"
        )