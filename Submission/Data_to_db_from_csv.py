import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import MapPets, Base

engine = create_engine('sqlite:///restaurant_details.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()
import csv

session.query(MapPets).delete()

def extract_data_from_csv():
    a = []
    b = []
    with open('output_data.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if(len(row['latitude']) >= 2):
                a.append([row['latitude'], row['longitude']])
            else:
                a.append([0,0])
    with open('Crawled_Data.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            b.append([row['URL'], row['Name'],row['Rating'],row['Address']])
    return(a,b)

picture = ["http://imgur.com/yI00Ehb.jpg",\
           "http://i.imgur.com/TtmYVK2.jpg",\
           "http://i.imgur.com/EFN7FTv.jpg",\
           "http://i.imgur.com/RpD34tu.jpg",\
           "http://i.imgur.com/ryCH0b5.jpg",\
           "http://i.imgur.com/kzi5kKy.jpg",\
           "http://i.imgur.com/bOfNUzK.jpg",\
           "http://i.imgur.com/vtb1WCH.jpg",\
           "http://i.imgur.com/xrfHjtK.jpg",\
           "http://i.imgur.com/z7JCSX8.jpg",\
           ]

color = ["#E44040", "#EC21C7", "#8C4C80", "#A41FEC", "#B99ADA"\
    , "#4E15E9", "#154EE9", "#4B9CF8", "#65BCD8", "#13EFE4"\
    , "#13EFA2", "#13EF63", "#3E7753", "#8DBE1A", "#D6E6AE"\
    , "#E8F669", "#949478", "#E4B92C", "#E98915", "#F2802E"]

(a,b) = extract_data_from_csv()

for i in range(len(a)):
    print(i)
    if(a[i][0]!=1):
        Name = b[i][1]
        Picture = picture[random.randint(0, len(picture) - 1)]
        Color = color[random.randint(0, len(color) - 1)]
        Longitude = a[i][1]
        Latitude = a[i][0]
        Location = b[i][3]
        Ratings = b[i][2]
        URL = b[i][0]
        restaurant = MapPets(Name = Name, Picture = Picture, Color = Color, Longitude = Longitude, Latitude= Latitude, Location = Location, Ratings = Ratings, URL = URL)
        session.add(restaurant)
        session.commit()
    else:
        print("Latitude and Longitude not available")

print("added restaurants details!")
