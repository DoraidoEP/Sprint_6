import allure
from pages.main_page import MainPage
from conftest import driver
from data import TestData
import pytest


class TestMainPageFaq:
    @allure.title('Проверка раздела "Вопросы о важном"')
    @allure.description('Проверка на наличие нужного текста в выпадающих списках раздела')
    @pytest.mark.parametrize('question_number, expected_answer', TestData.test_data_question_answer)
    def test_click_faq_expand_icons_text_is_expected(self, driver, question_number, expected_answer):
        main_page = MainPage(driver)
        main_page.scroll_to_faq_section()
        main_page.wait_visibility_of_faq_items(question_number)
        main_page.click_on_faq_items(question_number)
        main_page.wait_visibility_of_faq_answer(question_number)
        assert main_page.get_displayed_text_from_faq_answer(question_number) == expected_answer
