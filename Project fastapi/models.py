from sqlalchemy import Column,Integer,String,Float,Primary_Key
from.database import Base
class Pet(Base):
    __tablename__='pets'
    id=Column(Integer,Primary_Key==True,index=True)
    name=Column(String,index=True)
    age=Column(Integer)
    type=Column(String)
    price=Column(Float)