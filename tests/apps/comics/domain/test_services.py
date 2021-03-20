from unittest import TestCase

from apps.comics.domain.entities import Comic
from apps.comics.domain.services import ObtainAmountToPayService


class ObtainAmountToPayServiceTest(TestCase):

    def setUp(self):
        self.obtain_amount_to_pay = ObtainAmountToPayService()
        self.comic = None

    def assertThatAmountToPayIs(self, amount):
        self.assertEqual(amount, self.obtain_amount_to_pay(self.comic))

    def test_excelent_comic_obtain_20_percentage_of_discount(self):
        self.comic = Comic(
            id=12,
            name="One Punch Man",
            price=20.0,
            status='excelent'
        )

        self.assertThatAmountToPayIs(18.0)

    def test_good_comic_obtain_20_percentage_of_discount(self):
        self.comic = Comic(
            id=12,
            name="One Punch Man",
            price=20.0,
            status='good'
        )

        self.assertThatAmountToPayIs(16.0)

    def test_acceptable_comic_obtain_25_percentage_of_discount(self):
        self.comic = Comic(
            id=12,
            name="One Punch Man",
            price=20.0,
            status='acceptable'
        )

        self.assertThatAmountToPayIs(15.0)        

    def test_imapaired_comic_obtain_30_percentage_of_discount(self):
        self.comic = Comic(
            id=12,
            name="One Punch Man",
            price=20.0,
            status='impaired'
        )

        self.assertThatAmountToPayIs(14.0)        

    def test_damaged_comic_obtain_50_percentage_of_discount(self):
        self.comic = Comic(
            id=12,
            name="One Punch Man",
            price=20.0,
            status='damaged'
        )

        self.assertThatAmountToPayIs(10.0)
