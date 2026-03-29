import random
import time
from database import users_db, orders_db


# ----------------------------
# USER CREATION
# ----------------------------
def create_user(user):

    # simulate database delay
    time.sleep(0.5)

    users_db[user.user_id] = user

    return {"message": "User created successfully"}


# ----------------------------
# PAYMENT SYSTEM
# ----------------------------
def process_payment(order):

    # simulate delay (network / payment gateway)
    time.sleep(1)

    # randomly fail
    if random.choice([True, False]):
        raise Exception("Payment gateway failure")

    return True


# ----------------------------
# EXTERNAL API CALL
# ----------------------------
def call_external_api():

    # simulate delay
    time.sleep(1)

    # always fail (timeout scenario)
    raise Exception("External API timeout")


# ----------------------------
# ORDER PROCESSING
# ----------------------------
def process_order(order):

    if order.amount <= 0:
        raise ValueError("Invalid order amount")

    # Step 1: payment
    process_payment(order)

    # Step 2: external service
    call_external_api()

    # Step 3: store order
    orders_db[order.order_id] = order

    return {"message": "Order completed"}