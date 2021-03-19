from datetime import datetime, timedelta

from .vo import ComicId


class Comic:
    def __init__(self, id, name, price, status):
        self._id = ComicId(id)
        self.name = name
        self.price = price
        self.status = status

    @property
    def id(self):
        return self._id.value
    

class Rent:
    def __init__(self, id, days, client, rented_at, comicId: ComicId, finished_at=None, price=None, amount=None):
        self.id = id
        self.days = int(days)
        self.client = client
        self.rented_at = rented_at
        self.comicId = comicId
        self.finished_at = finished_at
        self.price = price
        self.amount = amount

    @property
    def get_finished_at(self):
        transform = datetime.strptime(self.rented_at, '%Y-%m-%d %H:%M:%S')
        _finished_at = transform + timedelta(days=self.days)
        return _finished_at
