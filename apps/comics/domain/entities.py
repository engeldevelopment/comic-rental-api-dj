from dataclasses import dataclass


@dataclass
class ComicId:
    value: str


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
