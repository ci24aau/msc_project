from pydantic import BaseModel


# User model (data validation)
class User(BaseModel):
    user_id: int
    name: str
    email: str


# Order model
class Order(BaseModel):
    order_id: int
    user_id: int
    amount: float