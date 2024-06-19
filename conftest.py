import pytest
from selenium import webdriver
from data import TestData

@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.set_window_size(1920, 1080)
    driver.get(TestData.scooter_address)
    yield driver
    driver.quit()