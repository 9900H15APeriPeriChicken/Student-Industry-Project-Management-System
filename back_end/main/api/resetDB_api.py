from flask_restful import Resource
from back_end.main.extension import db
from back_end.main.models import User


def reset_db():
    db.drop_all()
    db.create_all()
    User.init_user()


class resetDBView(Resource):
    def get(self):
        reset_db
        return {
            'code':200,
            'body': None,
            'msg': 'Database Reset!'
        }
