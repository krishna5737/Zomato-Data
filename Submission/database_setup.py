import sys
from sqlalchemy import Column, ForeignKey, Integer, String,Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


Base = declarative_base()

class MapPets(Base):
    __tablename__ = 'MapPets'
    Id = Column(Integer, primary_key=True)
    Name = Column(String(64))
    Picture = Column(String(128))
    Color= Column(String(32))
    Longitude = Column(Integer)
    Latitude = Column(Integer)
    Location = Column(String(256))
    Ratings = Column(String(5))
    URL =  Column(String(128))

engine = create_engine('sqlite:///restaurant_details.db')
Base.metadata.create_all(engine)
