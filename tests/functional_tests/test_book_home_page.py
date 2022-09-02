import time
from unittest import skip
import pytest 
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.by import By
from utils.browser import make_chrome_browser


class BookBaseFunciontalTest(StaticLiveServerTestCase):
    def setUp(self) -> None:
        self.browser = make_chrome_browser()
        return super().setUp()

    def tearDown(self) -> None:
        self.browser.quit()
        return super().tearDown()

    def sleep(self, seconds=5):
        time.sleep(seconds)


@pytest.mark.functional_test
class BookHomePageFunctionalTest(BookBaseFunciontalTest):
    @skip('Pular por enqto...chromedriver...')
    def test_book_home_page_without_books_error_message(self):
        """Se SELENIUM_HEADLESS em .env = 1 não abre o navegador"""
        self.browser.get(self.live_server_url)
        body = self.browser.find_element(By.TAG_NAME, 'body')
        self.assertIn('No books found here 🥲', body.text)
       
