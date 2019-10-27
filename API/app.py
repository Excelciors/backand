# -*- coding: latin-1 -*-
import sys
sys.path.append('../')

import ast
from flask_restful import reqparse
from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask import jsonify
import psycopg2
import requests
from flask_cors import CORS, cross_origin
from collections import OrderedDict
import hashlib
from hashlib import md5
import requests
import json
import numpy as np
import config
import sqlalchemy
import functions


from flask_jwt_extended import JWTManager

from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)


def computeMD5hash(my_string):
    m = hashlib.md5()
    m.update(my_string.encode('utf-8'))
    return m.hexdigest()


app = Flask(__name__)
api = Api(app)
CORS(app)

connection = config.DATABASE_URI

parser = reqparse.RequestParser()

# class UserLogin(Resource):
#     def post(self):
#         data = parser.parse_args()
#         current_user = UserModel.find_by_username(data['username'])

#         if not current_user:
#             return {'message': 'User {} doesn\'t exist'.format(data['username'])}
        
#         if UserModel.verify_hash(data['password'], current_user.password):
#             access_token = create_access_token(identity = data['username'])
#             refresh_token = create_refresh_token(identity = data['username'])
#             return {
#                 'message': 'Logged in as {}'.format(current_user.username),
#                 'access_token': access_token,
#                 'refresh_token': refresh_token
#                 }
#         else:
#             return {'message': 'Wrong credentials'}


class UserLogin(Resource):
	def post(self):
		parser.add_argument('login', type=str)
		parser.add_argument('senha', type=str)
		data = parser.parse_args()


		login = data['login']
		senha = data['senha']

		return functions.UserLogin.login(self,login,senha)




class InsertUser(Resource):
	def post(self):
		parser.add_argument('dados_usuario', type=str)
		args = parser.parse_args()
		
		dados = ast.literal_eval(args['dados_usuario'])


		functions.inserts.user(self, dados)
	
		return "sucesso"

class GetAllUsers(Resource):
	def get(self):
		retorno = functions.selects.allUsers(self)
		return retorno

class GetOneUser(Resource):
	def get(self,id):
		retorno = functions.selects.user(self,id)
		return retorno

class ModifyUser(Resource):
	#@jwt_required
	def get(self,id):
		parser.add_argument('dados_usuario', type=str)
		args = parser.parse_args()
		dados = ast.literal_eval(args['dados_usuario'])

		retorno = functions.modify.modifyUser(self,id,dados)
		return retorno



#conteúdo
class AddClass(Resource):
	def post(self):
		parser.add_argument('dados_conteudo', type=str)
		args = parser.parse_args()
		dados = ast.literal_eval(args['dados_conteudo'])

		retorno = functions.inserts.clas(self,dados)
		return retorno

class AddContent(Resource):
	def post(self):
		parser.add_argument('dados_conteudo', type=str)
		args = parser.parse_args()
		dados = ast.literal_eval(args['dados_conteudo'])

		retorno = functions.inserts.contents(self,dados)
		return retorno

class AddCuriosity(Resource):
	def post(self):
		parser.add_argument('dados_conteudo', type=str)
		args = parser.parse_args()
		dados = ast.literal_eval(args['dados_conteudo'])

		retorno = functions.inserts.curiosity(self,dados)
		return retorno

class GetClasses(Resource):
	def get(self):
		retorno = functions.selects.classes(self)
		return retorno

class GetConteudo(Resource):
	def get(self,id):
		retorno = functions.selects.conteudo(self,id)
		return retorno

class GetTopic(Resource):
	def get(self):
		retorno = functions.selects.topico(self)
		return retorno

class GetCuriosity(Resource):
	def get(self,id):
		retorno = functions.selects.curiosity(self,id)
		return retorno

class GetPermissao(Resource):
	def get(self):
		retorno = functions.selects.permissao(self)
		return retorno

class AddPermissao(Resource):
	def post(self):
		parser.add_argument('dados_permissao', type=str)
		args = parser.parse_args()
		dados = ast.literal_eval(args['dados_permissao'])

		retorno = functions.inserts.permissao(self,dados)
		return retorno


#apis usuário
api.add_resource(InsertUser, '/user/add_user')
api.add_resource(GetAllUsers, '/user/get_all')
api.add_resource(GetOneUser, '/user/get_one/<id>')
api.add_resource(ModifyUser, '/user/modify/<id>')


#apis conteúdo
api.add_resource(AddClass, '/content/add_class')
api.add_resource(AddContent, '/content/add_content')
api.add_resource(AddCuriosity, '/content/add_curiosity')
api.add_resource(GetClasses, '/content/get_classes')
api.add_resource(GetConteudo, '/content/get_conteudo/<id>')
api.add_resource(GetTopic, '/content/get_topic')
api.add_resource(GetCuriosity, '/content/get_curiosity/<id>')

#api.permissao
api.add_resource(AddPermissao, '/permissao/add_permissao')
api.add_resource(GetPermissao, '/permissao/get_permissao')


#Login
api.add_resource(UserLogin, '/login')




if __name__ == '__main__':
	app.run(port='3333')

