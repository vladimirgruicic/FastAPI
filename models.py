from pydantic import BaseModel

# Model for item.
class Item(BaseModel):
    name: str
    price: float
    quantity: int

# Model for user.
class User(BaseModel):
    username: str
    email: str

class user_request(BaseModel):
    username: str
    email: str
    user_request: str