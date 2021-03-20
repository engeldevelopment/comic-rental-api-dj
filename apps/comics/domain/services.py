from injector import inject

from . import agregates
from .entities import Comic
from .vo import ComicId
from .repositories import ComicRepository


class ObtainAmountToPayService:
    def __call__(self, comic: Comic):
        discount = 0
        DISCOUNTS = {
            'excelent': agregates.ExcelentComicDiscount.forThis(comic=comic).apply(),
            'good': agregates.GoodComicDiscount.forThis(comic=comic).apply(),
            'acceptable': agregates.AcceptableComicDiscount.forThis(comic=comic).apply(),
            'impaired': agregates.ImpairedComicDiscount.forThis(comic=comic).apply(),
            'damaged': agregates.DamagedComicDiscount.forThis(comic=comic).apply()
        }

        discount = DISCOUNTS.get(comic.status)
        return comic.price - discount
