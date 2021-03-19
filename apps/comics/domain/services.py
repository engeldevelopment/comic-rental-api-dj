from injector import inject

from .entities import Comic
from .vo import ComicId
from .repositories import ComicRepository


class ObtainPercentOfDiscount:
    def __call__(self, price, percent):
        return (price * percent) / 100


class ObtainAmountToPayService:

    @inject
    def  __init__(self,
        repository: ComicRepository,
        percent_of_discount: ObtainPercentOfDiscount
    ):
        self.repository = repository
        self.percent_of_discount = percent_of_discount
    
    def __call__(self, comicId: ComicId):
        comic = self.repository.findById(id=comicId)
        discount = 0
        DISCOUNTS = {
            'excelent': self.percent_of_discount(price=comic.price, percent=10),
            'good': self.percent_of_discount(price=comic.price, percent=20),
            'acceptable': self.percent_of_discount(price=comic.price, percent=25),
            'impaired': self.percent_of_discount(price=comic.price, percent=30),
            'damaged': self.percent_of_discount(price=comic.price, percent=50)
        }

        discount = DISCOUNTS.get(comic.status)
        return comic.price - discount
