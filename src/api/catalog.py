from fastapi import APIRouter
import sqlalchemy
from src import database as db

router = APIRouter()


@router.get("/catalog/", tags=["catalog"])
def get_catalog():
    """
    Each unique item combination must have only a single price.
    """
    
    num_red = 0
    num_green = 0
    num_blue = 0

    with db.engine.begin() as connection:
        result = connection.execute(sqlalchemy.text("SELECT num_red_potions FROM potions"))
        num_red = result.first().num_red_potions
        result = connection.execute(sqlalchemy.text("SELECT num_green_potions FROM potions"))
        num_green = result.first().num_green_potions
        result = connection.execute(sqlalchemy.text("SELECT num_blue_potions FROM potions"))
        num_blue = result.first().num_blue_potions

    # Can return a max of 20 items.
    catalog = []

    if num_red > 0:
        catalog.append({
                "sku": "RED_POTION_0",
                "name": "red potion",
                "quantity": num_red,
                "price": 50,
                "potion_type": [100, 0, 0, 0],
            })
    if num_green > 0:
        catalog.append({
                "sku": "GREEN_POTION_0",
                "name": "green potion",
                "quantity": num_green,
                "price": 50,
                "potion_type": [0, 100, 0, 0],
            })
    if num_blue > 0:
        catalog.append({
                "sku": "BLUE_POTION_0",
                "name": "blue potion",
                "quantity": num_blue,
                "price": 50,
                "potion_type": [0, 0, 100, 0],
            })
    
    if catalog == []:
        return "no potions"
    else:
        return catalog



