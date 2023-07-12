from models import User
from fastapi import APIRouter
from database import get_db

#Initalize router.
router = APIRouter()

# Create users.
@router.post("/users")
def create_user(user: User):
    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        "INSERT INTO users (username, email) VALUES (?, ?)",
        (user.username, user.email)
    )
    db.commit()

    return {"message": "User created sucessfully!"}
