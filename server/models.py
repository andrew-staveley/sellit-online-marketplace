from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import validates
from config import db, bcrypt

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'
    serialize_rules = ('-listings', '-reviews', '-_password_hash')

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    _password_hash = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    bio = db.Column(db.String)
    city = db.Column(db.String)
    state = db.Column(db.String, nullable=False)
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
    
class Listing(db.Model, SerializerMixin):
    __tablename__ = 'listings'
    serialize_rules = ('-reviews')
    
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String)
    description = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    user = db.Column(db.Integer, db.ForeignKey('users.id'))
    reviews = db.relationship('Review', backref='listing')

class Review(db.Model):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String, nullable=False)
    user = db.Column(db.Integer, db.ForeignKey('users.id'))
    listing = db.Column(db.Integer, db.ForeignKey('listings.id'))
    
