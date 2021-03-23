from datetime import datetime, timedelta

import uuid

from .vo import ComicId, ComicStatus


class Comic:
    def __init__(self, id, name, price, status: ComicStatus):
        self._id = ComicId(id)
        self.name = name
        self.price = price
        self.status = status

    @property
    def id(self):
        return self._id.value
    

class Rental:
    def __init__(self, id, days, client, rented_at, comic_id: ComicId, finished_at=None, price=None, amount=None):
        self.id = self.generate_uuid(id)
        self.days = int(days)
        self.client = client
        self.rented_at = rented_at
        self.comicId = comic_id
        self.finished_at = finished_at
        self.price = price
        self.amount = amount
    
    def generate_uuid(self, id):
        generated_id = id
        if id is None:
            generated_id = uuid.uuid4()
        return generated_id

    @property
    def get_finished_at(self):
        transform = datetime.strptime(self.rented_at, '%Y-%m-%d %H:%M:%S')
        _finished_at = transform + timedelta(days=self.days)
        return _finished_at
    
    @property
    def to_json(self):
        return {
            'id': self.id,
            'client': self.client,
            'days': self.days,
            'price': self.price,
            'amount': self.amount,
            'comicId': self.comicId.value,
            'rented_at': self.rented_at,
            'finished_at': self.finished_at
        }
