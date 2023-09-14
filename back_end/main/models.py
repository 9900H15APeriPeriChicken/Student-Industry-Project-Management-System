from back_end.main.extension import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.Integer)

    # Admin-0, Students-1, Academic Supervisors-2, Industry Partners-3

    @staticmethod
    def init_user():
        result = User.query.filter_by(username='admin').first()
        print("Admin User ", "Found" if result is not None else  "Not Found" )
        if result is None:
            admin_user = User()
            admin_user.id = 0
            admin_user.username = 'admin'
            admin_user.password = 'admin'
            admin_user.role = 0
            db.session.add(admin_user)
            db.session.commit()

    @property
    def password(self):
        raise AttributeError('password is not readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "<Users {}>".format(self.username)
