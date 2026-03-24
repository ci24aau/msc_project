from database import users_db, orders_db
import random
import time

def create_user(user):

    users_db[user.user_id] = user

    return {
        "message": "User created successfully"
    }


def process_order(order):

    if order.amount <= 0:
        raise ValueError("Invalid order amount")

    orders_db[order.order_id] = order

    return {
        "message": "Order processed successfully"
    }

def process_payment(order):

    time.sleep(1)  # simulate delay

    if random.choice([True, False]):
        raise Exception("Payment gateway failure")

    return True


def call_external_service():

    time.sleep(1)

    raise Exception("External API timeout")