from fastapi import FastAPI,Depends,HTTPException
from sqlalchemy.orm import Session
from.import models,schemas
from.database import SessionLocal,engine
models.Base.metadata.create_all(bind=engine)
app=FastAPI()
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.post('/pets/',response_model=schemas.Pet)
def create_pet(pet:schemas.PetCreate,db:Session=Depends(get_db)):
    db_pet=models.Pet(**pet.dict())
    db.add(db_pet)
    db.commit()
    db.refresh(db_pet)
    return db_pet
@app.get('/pets/',response_model=list[schemas.Pet])
def read_pets(skip:int=0,limit:int=10,db:Session=Depends(get_db)):
    pets=db.query(models.Pet).offset(skip).limit(limit).all()
    return pets
@app.get('/pets/{pet_id}',response_model=schemas.Pet)
def read_pet(pet_id:int,db:Session=Depends(get_db)):
    pet=db.query(models,pet).filter(models.Pet.id==pet_id).first()
    if pet in None:
        raise HTTPException(status_code=404,detail='pet not found')
    return pet
@app.put('/pets/{pet_id}',response_model=schemas.Pet)
def update_pet(pet_id:int,pet:schemas.PetCreate,db:Session=Depends(get_db)):
    db_pet=db.query(models.Pet).filter(models.Pet.id==pet_id).first()
    if db_pet is None:
        raise HTTPException(status_code=404,detail='pet not found')
    for key,value in pet.dict().items():
        setattr(db_pet,key,value)
        db.commit()
        db.refresh(db_pet)
        return db_pet
@app.delete('/pets/{pet_id}',response_model=schemas.Pet)
def delete_pet(pet_id:int,db:Session=Depends(get_db)):
    db_pet=db.query(models.Pet).filter(models.pet.id==pet_id).first()
    if db_pet is None:
        raise HTTPException(status_code=404,detail='pet not found')
    db.delete(db_pet)
    db.commit()
    return db_pet