from app.persistence.repository import InMemoryRepository


class HBnBFacade:
    def __init__(self):
        self.repository = InMemoryRepository()

    def get_repository(self):
        return self.repository