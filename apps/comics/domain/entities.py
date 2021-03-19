from .vo import ComicId


class Comic:
    def __init__(self, id, name, price, status):
        self.id = ComicId(id)
        self.name = name
        self.price = price
        self.status = status

    @property
    def id(self):
        return self.id.value
    
    @id.setter
    def id(self, value):
        self.id = ComicId(value)


class Rent:
    def __init__(self, id, days, client, rented_at, comicId: ComicId):
        self.id = id
        self.days = days
        self.client = client
        self.rented_at = rented_at
        self.comicId = comicId
