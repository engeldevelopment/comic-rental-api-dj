from . import agregates
from .entities import Comic
from .vo import ComicStatus


class ObtainAmountToPayService:
    def __call__(self, comic: Comic):
        DISCOUNTS = {
            ComicStatus.EXCELLENT: agregates.ExcellentComicDiscount.for_this(comic=comic).apply(),
            ComicStatus.GOOD: agregates.GoodComicDiscount.for_this(comic=comic).apply(),
            ComicStatus.ACCEPTABLE: agregates.AcceptableComicDiscount.for_this(comic=comic).apply(),
            ComicStatus.IMPAIRED: agregates.ImpairedComicDiscount.for_this(comic=comic).apply(),
            ComicStatus.DAMAGED: agregates.DamagedComicDiscount.for_this(comic=comic).apply()
        }

        discount = DISCOUNTS.get(comic.status)
        return comic.price - discount
