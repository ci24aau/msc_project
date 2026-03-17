from pydantic import BaseModel


class User(BaseModel):
    user_id: int
    name: str
    email: str


class Order(BaseModel):
    order_id: int
    user_id: int
    amount: float