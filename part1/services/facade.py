from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity


class HBnBFacade:
    def __init__(self):
        self.users = InMemoryRepository()
        self.places = InMemoryRepository()
        self.reviews = InMemoryRepository()
        self.amenities = InMemoryRepository()

    # USERS
    def create_user(self, data):
        user = User(**data)
        self.users.add(user)
        return user

    def get_users(self):
        return self.users.get_all()

    # PLACES
    def create_place(self, data):
        place = Place(**data)
        self.places.add(place)
        return place

    def get_places(self):
        return self.places.get_all()

    # REVIEWS
    def create_review(self, data):
        review = Review(**data)
        self.reviews.add(review)
        return review

    # AMENITIES
    def create_amenity(self, data):
        amenity = Amenity(**data)
        self.amenities.add(amenity)
        return amenity
