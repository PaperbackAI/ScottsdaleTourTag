from fastapi import APIRouter, Depends, BackgroundTasks
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud import get_home_listings
from app.schemas import HomeListingResponse
from app.background_tasks import update_home_listings

router = APIRouter()

@router.get("/listings", response_model=list[HomeListingResponse])
def read_listings(db: Session = Depends(get_db)):
    return get_home_listings(db)

@router.post("/update-listings")
def trigger_update(background_tasks: BackgroundTasks):
    background_tasks.add_task(update_home_listings)
    return {"message": "Home listings update started in the background"}
