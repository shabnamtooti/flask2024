from pydantic import BaseModel
class PetBase(BaseModel):
    name:str
    age:int
    type:str
    price:float
class PetCreate(PetBase):
    pass
class Pet(PetBase):
    id:int
    class Config:
        orm_mode=True