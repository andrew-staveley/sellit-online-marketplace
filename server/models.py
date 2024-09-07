from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import validates
from config import db, bcrypt

from config import db

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'
    serialize_rules = ('-listings', '-_password_hash')

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique='True')
    _password_hash = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    bio = db.Column(db.String)
    city = db.Column(db.String)
    state = db.column(db.String, nullable=False)
    reviews = db.relationship('Review', backref='user')
    listings = db.relationship('Listing', backref='user')

    @hybrid_property
    def password_hash(self):
        raise AttributeError('Password hashes may not be viewed')
    
    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(password.encode('utf-8'))
        self._password_hash = password_hash = password_hash.decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(self._password_hash, password.encode('utf-8'))
