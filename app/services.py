import random
import time
from database import users_db, orders_db


# ---------------------------
# USER CREATION
# ---------------------------
def create_user(user):

    time.sleep(0.5)  # simulate database delay

    users_db[user.user_id] = user

    return {"message": "User created successfully"}


# ---------------------------
# PAYMENT SYSTEM (SIMULATED)
# ---------------------------
def process_payment(order):

    time.sleep(1)  # simulate network delay

    # randomly fail
    if random.choice([True, False]):
        raise Exception("Payment gateway failure")

    return True


# ---------------------------
# EXTERNAL API (SIMULATED)
# ---------------------------
def call_external_service():

    time.sleep(1)

    raise Exception("External API timeout")


# ---------------------------
# ORDER PROCESSING
# ---------------------------
def process_order(order):

    if order.amount <= 0:
        raise ValueError("Invalid order amount")

    # Step 1: simulate payment
    process_payment(order)

    # Step 2: simulate external API call
    call_external_service()

    # Step 3: store order
    orders_db[order.order_id] = order

    return {"message": "Order completed"}