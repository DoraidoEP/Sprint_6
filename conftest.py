import pytest
from selenium import webdriver
from data import UrlData

@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.set_window_size(1920, 1080)
    driver.get(UrlData.scooter_address)
    yield driver
    driver.quit()