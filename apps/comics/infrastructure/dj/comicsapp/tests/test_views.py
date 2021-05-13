from datetime import datetime

from uuid import uuid4

from rest_framework import status
from rest_framework.test import APITestCase

from apps.comics.domain.vo import ComicStatus
from ..factories import ComicFactory
from ..models import Rental


class ComicListAPIViewTest(APITestCase):
    def setUp(self):
        self.url = '/api/v1/comics'
        self.status_url = "/api/v1/comics?status={0}"

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
    
    def test_filter_comics_by_status(self):
        ComicFactory.create(status=ComicStatus.ACCEPTABLE.value)

        response = self.client.get(self.status_url.format(ComicStatus.ACCEPTABLE.value))

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(1, len(response.data))

    def test_there_arent_comics_with_this_status(self):
        ComicFactory.create(status=ComicStatus.ACCEPTABLE.value)

        response = self.client.get(self.status_url.format(ComicStatus.EXCELLENT.value))

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(0, len(response.data))


class RentComicAPIViewTest(APITestCase):
    def setUp(self):
        self.comic = ComicFactory(name='A Comic')

    def test_rent_a_good_comic_with_discount_of_20_percent(self):
        comic = ComicFactory.create(
            price=20,
            status=ComicStatus.GOOD.value
        )

        data = {
            'id': self.generate_uuid(),
            'days': "3",
            'client': "Engel Pinto",
            'rented_at': datetime(2020, 4, 25)
        }        

        response = self.do_post_with(
            id=comic.id,
            data=data
        )

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertDayOfFinishedAtIs(28)
        self.assertAmountOfRentalIs(16.0)
    
    def test_when_i_do_not_give_an_id_to_the_rent_it_should_also_be_created(self):
        comic = ComicFactory.create(
            price=20,
            status=ComicStatus.ACCEPTABLE.value
        )

        data = {
            'days': "2",
            'client': "Javier Ortiz",
            'rented_at': datetime(2020, 12, 4)
        }

        response = self.do_post_with(
            id=comic.id,
            data=data
        )

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertDayOfFinishedAtIs(6)
        self.assertAmountOfRentalIs(15.0)

    def test_when_i_do_not_give_an_id_and_rented_at_to_the_rent_it_should_also_be_created(self):
        comic = ComicFactory.create(
            price=20,
            status=ComicStatus.ACCEPTABLE.value
        )

        data = {
            'days': "2",
            'client': "Javier Ortiz",
        }

        response = self.do_post_with(
            id=comic.id,
            data=data
        )

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertAmountOfRentalIs(15.0)

    def test_when_id_is_not_assigned_to_a_comic_give_an_error(self):
        data = {
            'days': "3",
            'client': "Engel Pinto"
        }

        response = self.do_post_with(
            id=0,
            data=data
        )

        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)

    def test_when_the_days_to_be_negative_should_give_an_error(self):
        data = {
            'days': "-3",
            'client': "Engel Pinto"
        }

        response = self.do_post_with(
            id=self.comic.id,
            data=data
        )

        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
        self.assertEqual("This is not a valid days '-3'.", response.data['message'])

    def test_if_not_pass_a_client_should_give_an_error(self):
        data = {
            'days': "3",
            'client': ""
        }

        response = self.do_post_with(
            id=self.comic.id,
            data=data
        )

        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
        self.assertEqual("This is not a valid name for a client ''.", response.data['message'])

    def test_if_the_name_for_client_is_numeric_should_give_an_error(self):
        data = {
            'days': "3",
            'client': "12884"
        }

        response = self.do_post_with(
            id=self.comic.id,
            data=data
        )

        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
        self.assertEqual("This is not a valid name for a client '12884'.", response.data['message'])

    @staticmethod
    def generate_url(for_id):
        return '/api/v1/comics/{0}/rentals/'.format(for_id)
    
    @staticmethod
    def generate_uuid():
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


class RentalListAPIViewTest(APITestCase):
    def setUp(self):
        self.url = "/api/v1/rentals"

    def test_if_there_arent_rentals_should_show_a_empty_list(self):
        response = self.client.get(self.url)

        self.assertEqual([], response.data)

    def test_if_there_are_rentals_should_show_it(self):
        data = {
            "days": "3",
            "client": "I am"
        }
        comic = ComicFactory.create()

        rent_url = "/api/v1/comics/{0}/rentals/".format(comic.id)
        self.client.post(rent_url, data)

        response = self.client.get(self.url)

        self.assertEqual(1, len(response.data))
