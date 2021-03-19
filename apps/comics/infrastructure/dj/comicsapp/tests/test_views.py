from rest_framework import status
from rest_framework.test import APITestCase

from ..factories import ComicFactory


class ComicListAPIView(APITestCase):
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
