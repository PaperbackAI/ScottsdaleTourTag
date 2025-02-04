from sqlalchemy.orm import Session
from app.models import HomeListing

def get_home_listings(db: Session):
    return db.query(HomeListing).all()

def create_home_listing(db: Session, address: str, price: str, details: str):
    new_listing = HomeListing(address=address, price=price, details=details)
    db.add(new_listing)
    db.commit()
    db.refresh(new_listing)
    return new_listing
