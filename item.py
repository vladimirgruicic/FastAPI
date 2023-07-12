from models import Item
from fastapi import APIRouter
from database import get_db

#Initalize router.
router = APIRouter()

# This is route that creates item.
@router.post("/items")
def create_item(item: Item):
    db = get_db()
    cursor = db.cursor()
    
    cursor.execute(
        "INSERT INTO items (name, price, quantity) VALUES (?, ?, ?)",
        (item.name, item.price, item.quantity)
    )
    
    db.commit()
    
    return {"message": "Item created sucessfully!"}

# This is route that update item.
@router.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"message": f"Item with ID {item_id} updated sucessfully!"}

# This is route that delete item.
@router.delete("/items/{item_id}")
def delete_item(item_id: int):
     return {"message": f"Item with ID {item_id} deleted successfully"}
