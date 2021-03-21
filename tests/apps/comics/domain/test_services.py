from unittest import TestCase

from apps.comics.domain.entities import Comic
from apps.comics.domain.services import ObtainAmountToPayService
from apps.comics.domain.vo import ComicStatus


class ObtainAmountToPayServiceTest(TestCase):

    def setUp(self):
        self.obtain_amount_to_pay = ObtainAmountToPayService()
        self.comic = None

    def assertThatAmountToPayIs(self, amount):
        self.assertEqual(amount, self.obtain_amount_to_pay(self.comic))

    def test_excellent_comic_obtain_20_percentage_of_discount(self):
        self.comic = Comic(
            id=12,
            name="One Punch Man",
            price=20.0,
            status=ComicStatus.EXCELLENT.value
        )

        self.assertThatAmountToPayIs(18.0)

    def test_good_comic_obtain_20_percentage_of_discount(self):
        self.comic = Comic(
            id=12,
            name="One Punch Man",
            price=20.0,
            status=ComicStatus.GOOD.value
        )

        self.assertThatAmountToPayIs(16.0)

    def test_acceptable_comic_obtain_25_percentage_of_discount(self):
        self.comic = Comic(
            id=12,
            name="One Punch Man",
            price=20.0,
            status=ComicStatus.ACCEPTABLE.value
        )

        self.assertThatAmountToPayIs(15.0)        

    def test_impaired_comic_obtain_30_percentage_of_discount(self):
        self.comic = Comic(
            id=12,
            name="One Punch Man",
            price=20.0,
            status=ComicStatus.IMPAIRED.value
        )

        self.assertThatAmountToPayIs(14.0)        

    def test_damaged_comic_obtain_50_percentage_of_discount(self):
        self.comic = Comic(
            id=12,
            name="One Punch Man",
            price=20.0,
            status=ComicStatus.DAMAGED.value
        )

        self.assertThatAmountToPayIs(10.0)
