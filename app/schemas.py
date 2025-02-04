from pydantic import BaseModel

class HomeListingBase(BaseModel):
    address: str
    price: str
    details: str

class HomeListingCreate(HomeListingBase):
    pass

class HomeListingResponse(HomeListingBase):
    id: int

    class Config:
        orm_mode = True
