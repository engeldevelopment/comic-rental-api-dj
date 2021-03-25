from datetime import datetime, timedelta

from .vo import ComicId, ComicStatus, Days, UUID, RentedAt


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
    def __init__(self,
                 days,
                 client,
                 comic_id: ComicId,
                 rented_at,
                 id=None,
                 finished_at=None,
                 price=None,
                 amount=None):
        self._id = UUID(id)
        self._days = Days(days)
        self.client = client
        self._rented_at = RentedAt(rented_at)
        self.comicId = comic_id
        self.finished_at = finished_at
        self.price = price
        self.amount = amount

    @property
    def days(self):
        return self._days.value

    @property
    def rented_at(self):
        return self._rented_at.value

    @property
    def id(self):
        return self._id.value

    @property
    def get_finished_at(self):
        rented_at_str = self.datetime_without_microseconds(self.rented_at)
        rented_at = datetime.strptime(rented_at_str, '%Y-%m-%d %H:%M:%S')
        _finished_at = rented_at + timedelta(days=self.days)
        return _finished_at

    @staticmethod
    def datetime_without_microseconds(date):
        return str(date).split('.')[0]
    
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
