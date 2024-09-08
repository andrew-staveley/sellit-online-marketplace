from flask import request
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from config import app, db, api
from models import User, Listing, Review

class Signup(Resource):
    def post(self):
        pass

class Login(Resource):
    def post(self):
        pass

class Logout(Resource):
    def delete(self):
        pass

class CheckSession(Resource):
    def get(self):
        pass

class Listing(Resource):
    def get(self):
        # Gets all listings for specified user
        pass
    def post(self):
        # Creates listing under specified user
        pass
    def delete(self):
        # Deletes specifed listing (Creator Only)
        pass

class Listings(Resource):
    def get(self):
        # Gets all listings
        pass

class Review(Resource):
    def get(self):
        # Retrives all reviews for specified user
        pass
    def post(self):
        # Creates review
        pass
    def delete(self):
        # Deltes review
        pass

class ItemReviews(Resource):
    def get(self):
        # Returns all item specific reviews
        pass

class User(Resource):
    def get(self):
        # Returns some user specific data
        pass

api.add_resource(Signup, '/signup', endpoint='signup')
api.add_resource(Login, '/login', endpoint='login')
api.add_resource(Logout, '/logout', endpoint='logout')
api.add_resource(CheckSession, '/check_session', endpoint='check_session')
api.add_resource(Listing, '/listing', endpoint='listing')
api.add_resource(Listings, '/listings', endpoint='listings')
api.add_resource(Review, '/review', endpoint='review')
api.add_resource(ItemReviews, '/item_reviews', endpoint='item_reviews')
api.add_resource(User, '/user', endpoint='user')

if __name__ == '__main__':
    app.run(port=5555, debug=True)

