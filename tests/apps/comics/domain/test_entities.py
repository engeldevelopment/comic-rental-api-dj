from unittest import TestCase

from apps.comics.domain.vo import ComicStatus
from tests.apps.comics.factories import ComicFactory


class ComicTest(TestCase):
    def setUp(self):
        self.comic = ComicFactory()

    def assertThatStatusIs(self, status: ComicStatus):
        self.assertEqual(status, self.comic.status)

    def test_the_states_is_excellent(self):
        self.comic = ComicFactory(
            status=ComicStatus(value='excellent')
        )
        self.assertThatStatusIs(ComicStatus.EXCELLENT)

    def test_the_status_is_good(self):
        self.comic = ComicFactory(
            status=ComicStatus(value='good')
        )
        self.assertThatStatusIs(ComicStatus.GOOD)

    def test_the_status_is_acceptable(self):
        self.comic = ComicFactory(
            status=ComicStatus(value='acceptable')
        )
        self.assertThatStatusIs(ComicStatus.ACCEPTABLE)

    def test_the_status_is_impaired(self):
        self.comic = ComicFactory(
            status=ComicStatus(value='impaired')
        )
        self.assertThatStatusIs(ComicStatus.IMPAIRED)

    def test_the_status_is_damaged(self):
        self.comic = ComicFactory(
            status=ComicStatus(value='damaged')
        )
        self.assertThatStatusIs(ComicStatus.DAMAGED)
