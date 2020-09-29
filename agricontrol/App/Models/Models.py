from App import db
from alembic import op
class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column('username',db.String, unique=True)
    password = db.Column(db.String)
    nivelAcesso = db.Column(db.Integer)
    email = db.Column(db.String)
    name = db.Column(db.String)
    fingerimage = db.Column(db.String)

    def __init__(self, username, password, name, fingerimage, email, nivelAcesso):
        self.username = username
        self.password = password
        self.nivelAcesso = nivelAcesso
        self.email = email
        self.name = name
        self.fingerimage = fingerimage

    def __repr(self):
        # return self.password
        return "<Userrrr %r>" % self.password
# --------------------------------------------------------------
class Producer(db.Model):
    __tablename__ = "producers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    farming = db.Column(db.String)
    annualamount = db.Column(db.Integer)
    pesticide = db.Column(db.String)

    def __init__(self, name, farming, annualamount, pesticide):
        self.name = name
        self.farming = farming
        self.annualamount = annualamount
        self.pesticide = pesticide

    def __repr(self):
        return "<Producer %r>" % self.name