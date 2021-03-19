from django.test import TestCase

from ..factories import ComicFactory


class ComicTest(TestCase):
    def test_excelent_comic_with_discount_of_10_percent(self):
        comic = ComicFactory.create(
            price=20.0,
            status='excelent'
        )
        self.assertEqual(18.0, comic.price_with_discount)

    def test_good_comic_with_discount_of_20_percent(self):
        comic = ComicFactory.create(
            price=20.0,
            status='good'
        )
        self.assertEqual(16.0, comic.price_with_discount)

    def test_acceptable_comic_with_discount_of_25_percent(self):
        comic = ComicFactory.create(
            price=20.0,
            status='acceptable'
        )
        self.assertEqual(15.0, comic.price_with_discount)

    def test_impaired_comic_with_discount_of_30_percent(self):
        comic = ComicFactory.create(
            price=20.0,
            status='impaired'
        )
        self.assertEqual(14.0, comic.price_with_discount)

    def test_damaged_comic_with_discount_of_50_percent(self):
        comic = ComicFactory.create(
            price=20.0,
            status='damaged'
        )
        self.assertEqual(10.0, comic.price_with_discount)
    