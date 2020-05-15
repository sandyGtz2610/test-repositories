import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel



#Clase recurso para registrarse
class UserRegister(Resource):
	parser = reqparse.RequestParser()
	#Se definen los argumentos permitidos en el json
	parser.add_argument('username',
		type=str,
		required=True,
		help="This fiels cannot be left blank"
	)
	parser.add_argument('password',
		type=str,
		required=True,
		help="This fiels cannot be left blank"
	)

	def post(self):
		data = UserRegister.parser.parse_args()
		if UserModel.find_by_username(data['username']):
			return {"message": "A user with that username already exists"}, 400

		user = UserModel(data['username'],data['password'])
		user.save_to_db()

		return {"message": "User created succesfully."}, 201
