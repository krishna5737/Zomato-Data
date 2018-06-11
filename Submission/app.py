from flask import *
from dbModel import *
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

engine = create_engine('sqlite:///restaurant_details.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/api", methods=['POST'])
def api():
    db_data = session.query(MapPets).all()
    infornation_dic = {}
    count = 0
    infornation_list = []
    print(db_data)
    for data in db_data:
        print(count)
        infornation_dic['data'] = []
        infornation_dic['Name'] = data.Name
        infornation_dic['Picture'] = data.Picture
        infornation_dic['Color'] = data.Color
        infornation_dic['Longitude'] = data.Longitude
        infornation_dic['Latitude'] = data.Latitude
        infornation_dic['Location'] = data.Location
        infornation_dic['Ratings'] = data.Ratings
        infornation_dic['URL'] = data.URL
        infornation_list.append(infornation_dic)
        infornation_dic = {}
    return json.dumps(infornation_list)


if __name__ == '__main__':
    app.run(debug=True)
