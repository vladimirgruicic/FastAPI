from fastapi import APIRouter
from models import user_request
from database import get_db

# Initialize router
router = APIRouter()

# Create user requests.
@router.post("/user_requests")
def create_user_request(user_request: user_request):
    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        "INSERT INTO user_requests (username, email, user_request) VALUES (?, ?, ?)",
        (user_request.username, user_request.email, user_request.user_request)
    )
    db.commit()

    return {"message": "User request created sucessfully!"}