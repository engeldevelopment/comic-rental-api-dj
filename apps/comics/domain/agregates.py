from .entities import Comic


class Discount:
    def __init__(self, comic: Comic):
        self.comic = comic
        self.percentage = 0

    @classmethod
    def for_this(cls, comic: Comic):
        return cls(comic=comic)

    def apply(self):
        return self.obtain_percentage(
            price=self.comic.price,
            percent=self.percentage
        )

    @staticmethod
    def obtain_percentage(price, percent):
        return (price * percent) / 100


class ExcellentComicDiscount(Discount):
    def __init__(self, comic: Comic):
        super().__init__(comic)
        self.percentage = 10


class GoodComicDiscount(Discount):
    def __init__(self, comic: Comic):
        super().__init__(comic)
        self.percentage = 20


class AcceptableComicDiscount(Discount):
    def __init__(self, comic: Comic):
        super().__init__(comic)
        self.percentage = 25


class ImpairedComicDiscount(Discount):
    def __init__(self, comic: Comic):
        super().__init__(comic)
        self.percentage = 30


class DamagedComicDiscount(Discount):
    def __init__(self, comic: Comic):
        super().__init__(comic)
        self.percentage = 50
