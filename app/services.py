from database import users_db, orders_db


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