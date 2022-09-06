import time
from unittest import skip

import pytest
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.by import By

from books.tests.test_book_base import BookMixin
from utils.browser import make_chrome_browser


class BookBaseFunciontalTest(StaticLiveServerTestCase, BookMixin):
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
    @skip("Pular por enqto...chromedriver...")
    def test_book_home_page_without_books_error_message(self):
        """Se SELENIUM_HEADLESS em .env = 1 não abre o navegador"""
        # self.make_book() -- para falhar
        # self.make_book_in_batch(qtd=10)
        self.browser.get(self.live_server_url)
        body = self.browser.find_element(By.TAG_NAME, "body")
        self.sleep()
        self.assertIn("No books found here 🥲", body.text)
