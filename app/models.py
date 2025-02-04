from sqlalchemy import Column, Integer, String
from app.database import Base

class HomeListing(Base):
    __tablename__ = "home_listings"
    
    id = Column(Integer, primary_key=True, index=True)
    address = Column(String, index=True)
    price = Column(String)
    details = Column(String)
