from fastapi import FastAPI
from database import initialize_database
from item import create_item, router as item_router
from user import create_user, router as user_router
from user_request import create_user_request, router as user_request_router

# App initialization.
app = FastAPI()

# Initalize the database for table items.
items_db = initialize_database()


# Include the Item router from item.py
app.include_router(item_router)

# Include the User router from user.py
app.include_router(user_router)

# Include the user_request router from user_request.py
app.include_router(user_request_router)

# Root route that needs to be modifed to represent the app.
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/items")
def create_item_route(item):
    return create_item(item)

@app.post("/users")
def create_user_route(user):
    return create_user(user)

@app.post("/user_requests")
def create_user_request_route(user_request):
    return create_user_request(user_request)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
