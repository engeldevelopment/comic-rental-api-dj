from . import agregates
from .entities import Comic


class ObtainAmountToPayService:
    def __call__(self, comic: Comic):
        DISCOUNTS = {
            'excelent': agregates.ExcelentComicDiscount.for_this(comic=comic).apply(),
            'good': agregates.GoodComicDiscount.for_this(comic=comic).apply(),
            'acceptable': agregates.AcceptableComicDiscount.for_this(comic=comic).apply(),
            'impaired': agregates.ImpairedComicDiscount.for_this(comic=comic).apply(),
            'damaged': agregates.DamagedComicDiscount.for_this(comic=comic).apply()
        }

        discount = DISCOUNTS.get(comic.status)
        return comic.price - discount
