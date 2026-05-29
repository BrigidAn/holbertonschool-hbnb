from app.models.base_model import BaseModel


class Review(BaseModel):
    def __init__(self, rating, comment, user_id, place_id):
        super().__init__()
        self.rating = rating
        self.comment = comment
        self.user_id = user_id
        self.place_id = place_id
