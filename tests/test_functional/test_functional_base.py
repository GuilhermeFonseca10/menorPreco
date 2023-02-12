import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import TestCase
from utils.browser import make_chrome_browser


class Base_test_functional_pages(TestCase, StaticLiveServerTestCase):
    def setUp(self) -> None:
        self.browser = make_chrome_browser()
        return super().setUp()

    def tearDown(self) -> None:
        self.browser.quit()
        return super().tearDown()

    def sleep(self, seconds=10):
        time.sleep(seconds)
