from django.test import TestCase

from apps.comics.domain.vo import ComicStatus
from ..forms import ComicForm


class ComicFormTest(TestCase):
    def setUp(self):
        self.data = {
            'name': 'A New Comic',
            'price': 100,
            'status': ComicStatus.ACCEPTABLE.value
        }

    def test_with_negative_price_should_not_to_be_valid(self):
        self.data['price'] = "-12.0"
        form = ComicForm(self.data)
        self.assertFalse(form.is_valid())

    def test_with_zero_price_should_not_to_be_valid(self):
        self.data['price'] = "0.0"
        form = ComicForm(self.data)
        self.assertFalse(form.is_valid())
