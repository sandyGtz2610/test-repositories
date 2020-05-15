from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from resources.user import UserRegister
from resources.f0101 import F0101
from resources.item import Item, ItemList
from resources.store import Store, StoreList
from security import authenticate, identity

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'jose'
api = Api(app)

@app.before_first_request
def create_tables():
	#Creará las tablas declaradas, a menos que ya existan
	db.create_all()


#Crea un endpoint que funciona con las funciones creadas 
#de authenticate e identity, y regersa un JWT
jwt = JWT(app, authenticate, identity)  #/auth

api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/items')
api.add_resource(Store,'/store/<string:name>')
api.add_resource(StoreList,'/stores')
api.add_resource(UserRegister,'/register')
api.add_resource(F0101,'/user/<string:an8>')

## Si en algun file.py queremos importar algo de éste archivp app.py
## con el if evita que se ejecut en cada importacion, a menos que lo 
## ejecute python app.py
if __name__ == '__main__':
	from db import db
	db.init_app(app)
	app.run(port=5000, debug=True)