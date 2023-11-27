from flask_restx import Api
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()
api = Api()
jwt = JWTManager()