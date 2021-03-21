from . import agregates
from .entities import Comic
from .vo import ComicStatus


class ObtainAmountToPayService:
    def __call__(self, comic: Comic):
        DISCOUNTS = {
            ComicStatus.EXCELLENT.value: agregates.ExcellentComicDiscount.for_this(comic=comic).apply(),
            ComicStatus.GOOD.value: agregates.GoodComicDiscount.for_this(comic=comic).apply(),
            ComicStatus.ACCEPTABLE.value: agregates.AcceptableComicDiscount.for_this(comic=comic).apply(),
            ComicStatus.IMPAIRED.value: agregates.ImpairedComicDiscount.for_this(comic=comic).apply(),
            ComicStatus.DAMAGED.value: agregates.DamagedComicDiscount.for_this(comic=comic).apply()
        }

        discount = DISCOUNTS.get(comic.status)
        return comic.price - discount
