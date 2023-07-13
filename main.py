from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from database import initialize_database, get_db
from item import create_item, router as item_router
from user import create_user, router as user_router
from user_request import create_user_request, router as user_request_router
from models import Item, User

# App initialization.
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Initialize the database.
initialize_database()

# Include the Item router from item.py
app.include_router(item_router)

# Include the User router from user.py
app.include_router(user_router)

# Include the user_request router from user_request.py
app.include_router(user_request_router)

# Root route that needs to be modified to represent the app.
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

# Route for retreiving items data from the database.
@app.get("/items_list")
def get_items(request: Request):
    db = get_db()
    cursor = db.cursor()

    cursor.execute("SELECT * FROM items")
    items = cursor.fetchall()

    return templates.TemplateResponse("items_list.html", {"request": request, "items": items})

# Route for inserting data with GET method which will give you interface for data insertion.
@app.get("/create_item")
def create_item_form(request: Request):
    return templates.TemplateResponse("create_item.html", {"request": request})

# Route for inserting data with POST method that will insert data into database.
@app.post("/create_item")
async def create_item_route(request: Request):
    form_data = await request.form()
    name = form_data.get("name")
    price = form_data.get("price")
    quantity = form_data.get("quantity")

    # Insert the data.
    item = Item(name=name, price=price, quantity=quantity)
    create_item(item)

    return templates.TemplateResponse("items_created.html", {"request": request, "item": item})

 # Route for retreiving items data from the database.   
@app.get("/users_list")
def get_users(request: Request):
    db = get_db()
    cursor = db. cursor()

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    return templates.TemplateResponse("users_list.html", {"request": request, "users": users})


@app.get("/create_user")
def create_user_form(request: Request):
    return templates.TemplateResponse("create_user.html", {"request": request})

@app.post("/create_user")
async def create_user_route(request: Request):
    form_data = await request.form()
    username = form_data.get("username")
    email = form_data.get("email")

    # Insert data.
    user = User(username=username, email=email)
    create_user(user)

    return templates.TemplateResponse("users_created.html", {"request": request, "user": user})