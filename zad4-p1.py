import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(autouse=True, scope="session")
def driver():
    _driver = webdriver.Chrome(executable_path = ChromeDriverManager().install())
    _driver.get('https://phptravels.com/flights-module-features/')
    yield _driver
    _driver.quit()


@pytest.mark.parametrize("header", [
    "Flight Listing",
    "Last Minutes Deal",
    "Popular Flights", ])
class TestClass:
    def test_headers_in_page_source(self, driver, header):
        assert(header in driver.page_source)
