from datetime import datetime

from uuid import uuid4

from rest_framework import status
from rest_framework.test import APITestCase

from ..factories import ComicFactory
from ..models import Rental


class ComicListAPIViewTest(APITestCase):
    def setUp(self):
        self.url = '/api/v1/comics'

    def test_show_a_comic_list(self):
        ComicFactory.create(name="DBZ")
        ComicFactory.create(name="One Punch Man")

        response = self.client.get(self.url)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(2, len(response.data))
    
    def test_there_arent_comics(self):

        response = self.client.get(self.url)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual([], response.data)


class RentComicAPIViewTest(APITestCase):
    def test_rent_a_good_comic_with_discount_of_20_percent(self):
        comic = ComicFactory.create(
            price=20,
            status='good'
        )

        data = {
            'id': self.generate_uuid(),
            'days': 3,
            'client': "Engel Pinto",
            'rented_at': datetime(2020, 4, 25)
        }        

        response = self.do_post_with(
            id=comic.id,
            data=data
        )
        rent = Rental.objects.last()

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertDayOfFinishedAtIs(28)
        self.assertAmountOfRentalIs(16.0)
    
    def test_when_i_do_not_give_an_id_to_the_rent_it_should_also_be_created(self):
        comic = ComicFactory.create(
            price=20,
            status='acceptable'
        )

        data = {
            'days': 2,
            'client': "Javier Ortiz",
            'rented_at': datetime(2020, 12, 4)
        }

        response = self.do_post_with(
            id=comic.id,
            data=data
        )

        rent = Rental.objects.last()

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertDayOfFinishedAtIs(6)
        self.assertAmountOfRentalIs(15.0)

    def test_when_id_is_not_assined_to_a_comic_give_an_error(self):
        data = {
            'days': 3,
            'client': "Engel Pinto",
            'rented_at': datetime(2020, 4, 25)
        }

        response = self.do_post_with(
            id=0,
            data=data
        )

        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)

    def generate_url(self, for_id):
        return '/api/v1/comics/{0}/rent/'.format(for_id)
    
    def generate_uuid(self):
        return uuid4()
    
    def do_post_with(self, id, data):
        return self.client.post(
            self.generate_url(id),
            data
        )
    
    def assertDayOfFinishedAtIs(self, day):
        rent = Rental.objects.last()
        self.assertEqual(day, rent.finished_at.day)
    
    def assertAmountOfRentalIs(self, amount):
        rent = Rental.objects.last()
        self.assertEqual(amount, rent.amount)