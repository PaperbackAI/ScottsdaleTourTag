from fastapi import APIRouter

router = APIRouter()

# Mock data for tourist points of interest
TOURIST_SPOTS = [
    {"name": "Desert Botanical Garden", "latitude": 33.4600, "longitude": -111.9484},
    {"name": "Taliesin West", "latitude": 33.6118, "longitude": -111.8466},
    {"name": "Old Town Scottsdale", "latitude": 33.4942, "longitude": -111.9261}
]

@router.get("/map-data")
def get_map_data():
    return {"tourist_spots": TOURIST_SPOTS}
