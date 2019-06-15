import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(autouse=True, scope="session")
def driver():
    _driver = webdriver.Chrome(executable_path = ChromeDriverManager().install())
    yield _driver
    _driver.quit()


@pytest.mark.parametrize("code, response", [
    ("200", "This page returned a 200 status code"),
    ("301", "This page returned a 301 status code"),
    ("404", "This page returned a 404 status code"),
    ("500", "This page returned a 500 status code")])
class TestClass:
    def test_headers_in_page_source(self, driver, code, response):
        driver.get('http://the-internet.herokuapp.com/status_codes/' + code)
        divContent = driver.find_element_by_xpath("//*[@id='content']/div/p").text
        assert(response in divContent)
