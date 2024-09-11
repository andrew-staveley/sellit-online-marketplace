from random import randint, choice as rc
from faker import Faker
from app import app
from models import User, Listing, Review, db

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")

        print("Deleting all records...")
        User.query.delete()
        Listing.query.delete()
        Review.query.delete()
        print("Record deletion complete.")

        print("Creating users...")
        users = []
        usernames = []
        for i in range(20):
            name = fake.first_name()
            username = name + fake.last_name()
            while username in usernames:
                username = fake.first_name()
            usernames.append(username)
            statelist = ['ME', 'NH', 'VT', 'MA', 'RI', 'CT', 'NY']
            citylist = ['Boston', 'Hartford', 'Providence', 'Manchester', 'New York City', 'Burlington', 'Portland']
            user = User(
                username=username,
                name=name,
                bio=fake.paragraph(nb_sentences=3),
                city=rc(citylist),
                state=rc(statelist),
            )
            user.password_hash = user.username + 'password'
            users.append(user)
        db.session.add_all(users)
        db.session.commit()
        print("Users have been created.")

        print("Creating listings...")
        listings = []
        for i in range(100):
            listing = Listing(
                item_name = rc(['Computer', 'iPhone', 'Adult Bike', '55" TV']),
                image = fake.image_url(),
                description = fake.paragraph(nb_sentences=2),
                price = randint(0, 1000),
            )
            listing.user = rc(users).id
            listings.append(listing)
        db.session.add_all(listings)
        db.session.commit()
        print("Listings have been create.")

        print("Creating reviews...")
        reviews = []
        for i in range(200):
            review = Review(
                rating = rc(range(5)),
                review_content = fake.paragraph(nb_sentences=2),
            )
            review.user = rc(users).id
            review.listing = rc(listings).id
            reviews.append(review)
        db.session.add_all(reviews)
        print("Reviews have been created.")

        print("Committing to database...")
        db.session.commit()
        print("Complete.")
            
    