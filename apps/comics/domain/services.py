from injector import inject

from .entities import Comic
from .vo import ComicStatus


class DiscountService:
    def __call__(self, comic: Comic):
        DISCOUNTS = {
            ComicStatus.EXCELLENT: ExcellentComicDiscount.for_this(comic=comic).apply(),
            ComicStatus.GOOD: GoodComicDiscount.for_this(comic=comic).apply(),
            ComicStatus.ACCEPTABLE: AcceptableComicDiscount.for_this(comic=comic).apply(),
            ComicStatus.IMPAIRED: ImpairedComicDiscount.for_this(comic=comic).apply(),
            ComicStatus.DAMAGED: DamagedComicDiscount.for_this(comic=comic).apply()
        }
        discount = DISCOUNTS.get(comic.status)
        return discount


class ObtainAmountToPayService:
    @inject
    def __init__(self, discount_service: DiscountService):
        self.discount_service = discount_service

    def __call__(self, comic: Comic):
        return comic.price - self.discount_service(comic)


class Discount:
    def __init__(self, comic: Comic):
        self.comic = comic
        self.percentage_of_discount = 0

    @classmethod
    def for_this(cls, comic: Comic):
        return cls(comic=comic)

    def apply(self):
        return self.obtain_percentage(
            price=self.comic.price,
            percent=self.percentage_of_discount
        )

    @staticmethod
    def obtain_percentage(price, percent):
        return (price * percent) / 100


class ExcellentComicDiscount(Discount):
    def __init__(self, comic: Comic):
        super().__init__(comic)
        self.percentage_of_discount = 10


class GoodComicDiscount(Discount):
    def __init__(self, comic: Comic):
        super().__init__(comic)
        self.percentage_of_discount = 20


class AcceptableComicDiscount(Discount):
    def __init__(self, comic: Comic):
        super().__init__(comic)
        self.percentage_of_discount = 25


class ImpairedComicDiscount(Discount):
    def __init__(self, comic: Comic):
        super().__init__(comic)
        self.percentage_of_discount = 30


class DamagedComicDiscount(Discount):
    def __init__(self, comic: Comic):
        super().__init__(comic)
        self.percentage_of_discount = 50
