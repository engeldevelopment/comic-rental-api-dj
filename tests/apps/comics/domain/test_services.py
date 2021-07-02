from unittest import TestCase

from apps.comics.domain.services import ObtainAmountToPayService, DiscountService
from apps.comics.domain.vo import ComicStatus


from tests.apps.comics.factories import ComicFactory


class ObtainAmountToPayServiceTest(TestCase):

    def setUp(self):
        self.obtain_amount_to_pay = ObtainAmountToPayService(DiscountService())
        self.comic = None

    def assertThatAmountToPayIs(self, amount):
        self.assertEqual(amount, self.obtain_amount_to_pay(self.comic))

    def test_excellent_comic_obtain_10_percentage_of_discount(self):
        self.comic = ComicFactory(
            price=20.0,
            status=ComicStatus.EXCELLENT
        )

        self.assertThatAmountToPayIs(18.0)

    def test_good_comic_obtain_20_percentage_of_discount(self):
        self.comic = ComicFactory(
            price=20.0,
            status=ComicStatus.GOOD
        )

        self.assertThatAmountToPayIs(16.0)

    def test_acceptable_comic_obtain_25_percentage_of_discount(self):
        self.comic = ComicFactory(
            price=20.0,
            status=ComicStatus.ACCEPTABLE
        )

        self.assertThatAmountToPayIs(15.0)        

    def test_impaired_comic_obtain_30_percentage_of_discount(self):
        self.comic = ComicFactory(
            price=20.0,
            status=ComicStatus.IMPAIRED
        )

        self.assertThatAmountToPayIs(14.0)        

    def test_damaged_comic_obtain_50_percentage_of_discount(self):
        self.comic = ComicFactory(
            price=20.0,
            status=ComicStatus.DAMAGED
        )

        self.assertThatAmountToPayIs(10.0)
