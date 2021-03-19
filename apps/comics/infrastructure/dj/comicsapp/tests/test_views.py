from datetime import datetime

from uuid import uuid4

from rest_framework import status
from rest_framework.test import APITestCase

from ..factories import ComicFactory
from ..models import Rent


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

        url = '/api/v1/comics/{0}/rent/'.format(comic.id)        
        uuid = str(uuid4())
        data = {
            'id': uuid,
            'days': 3,
            'client': "Engel Pinto",
            'rented_at': datetime(2020, 4, 25)
        }        

        response = self.client.post(url, data)

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        
    def test_when_id_is_not_assined_to_a_comic_give_an_error(self):
        url = '/api/v1/comics/{0}/rent/'.format(100)        
        data = {
            'id': 'id',
            'days': 3,
            'client': "Engel Pinto",
            'rented_at': datetime(2020, 4, 25)
        }

        response = self.client.post(url, data)

        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)
