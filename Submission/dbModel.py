from database_setup import *


class MapPets(Base):
    __tablename__ = 'MapPets'

    def __init__(self
                 , Name
                 , Picture
                 , Color
                 , Longitude
                 , Latitude
                 , Location
                 , Ratings
                 , URL,
                 ):
        self.Name = Name
        self.Picture = Picture
        self.Color = Color
        self.Longitude = Longitude
        self.Latitude = Latitude
        self.Location = Location
        self.Ratings = Ratings
        self.URL     = URL
