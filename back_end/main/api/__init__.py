from flask import Blueprint
from flask_restful import Api
from back_end.main.api import resetDB_api
from back_end.main.api.router import routes

api_bp = Blueprint('api', __name__)

api = Api(api_bp)
for uri in routes:
    api.add_resource(uri['component'], uri['path'])