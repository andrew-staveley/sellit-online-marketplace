from flask import request, session
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from config import app, db, api
from models import User, Listing, Review

class Signup(Resource):
    def post(self):
        req = request.get_json()
        username = req.get('username')
        password = req.get('password')
        name = req.get('name')
        bio = req.get('bio')
        city = req.get('city')
        state = req.get('state')

        user = User(
            username=username,
            name=name,
            bio=bio,
            city=city,
            state=state
        )
        user.password_hash = password
        try:
            db.session.add(user)
            db.session.commit()
            session['user_id'] = user.id
            return user.to_dict(), 201
        except IntegrityError:
            return {'error': 'Username is taken.'}, 422

class Login(Resource):
    def post(self):
        req = request.get_json()
        username = req.get('username')
        password = req.get('password')
        user = User.query.filter(User.username == username).first()
        if user:
            if user.authenticate(password):
                session['user_id'] = user.id
                return user.to_dict(), 200
            return {'error': 'Invalid Username or Password.'}, 401
        return {'error': 'Invalid Username or Password.'}, 401

class Logout(Resource):
    def delete(self):
        if session['user_id']:
            session['user_id'] = None
            return {}, 204
        else:
            return {'error': 'No active session to logout.'}, 401

class CheckSession(Resource):
    def get(self):
        if 'user_id' in session:
            user = User.query.filter(User.id == session.get('user_id')).first()
        else:
            return {"message": "401: Not Authorized"}, 401
        if user:
            return user.to_dict(), 201
        else:
            return {"message": "401: Not Authorized"}, 401

class Listing(Resource):
    def get(self):
        # Gets all listings for specified user
        pass
    def post(self):
        req = request.get_json()
        
        pass
    def delete(self):
        # Deletes specifed listing (Creator Only)
        pass

class Listings(Resource):
    def get(self):
        listings = Listing.query.all()
        if listings:
            return [listing.to_dict() for listing in listings], 200
        return {'error': '401: Unauthorized'}, 401

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

