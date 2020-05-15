from flask_restful import Resource, reqparse
from flask_jwt import jwt_required 
from models.f0101 import F0101Model

class F0101(Resource):
	@jwt_required() #Debemos autenticarnos para usar éste método
	def get(self, an8):
		f0101 = F0101Model.find_by_an8(an8)
		if f0101:
			return f0101.json()
		return {"message": "User not found"}, 404