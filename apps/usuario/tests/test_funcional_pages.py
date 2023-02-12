import pytest
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from utils.browser import make_chrome_browser


@pytest.mark.functional_test
class UsuarioPageFunctionalTest(StaticLiveServerTestCase):
    def test_main_login_page_text(self):
        browser = make_chrome_browser()
        browser.get(self.live_server_url)
        browser.maximize_window()
