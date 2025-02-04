from fastapi import APIRouter

router = APIRouter()

# Mock data for food locations
FOOD_LOCATIONS = [
    {"name": "The Mission Old Town", "latitude": 33.4928, "longitude": -111.9290, "cuisine": "Mexican"},
    {"name": "Cafe Monarch", "latitude": 33.4941, "longitude": -111.9295, "cuisine": "Fine Dining"},
    {"name": "Rehab Burger Therapy", "latitude": 33.4945, "longitude": -111.9298, "cuisine": "Burgers"}
]

@router.get("/food-finder")
def get_food_locations():
    return {"food_places": FOOD_LOCATIONS}
