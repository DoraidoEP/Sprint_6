import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Ожидание загрузки кнопки "Заказать" в шапке')
    def wait_visibility_of_order_button_in_header(self):
        self.wait_visibility_of_element(MainPageLocators.order_button_in_header)

    @allure.step('Клик по кнопке "Заказать" в шапке')
    def click_on_order_button_in_header(self):
        self.click_on_element(MainPageLocators.order_button_in_header)

    @allure.step('Ожидание загрузки лого "Самокат" в шапке')
    def wait_visibility_of_header_logo_scooter(self):
        self.wait_visibility_of_element(MainPageLocators.header_logo_scooter)

    @allure.step('Ожидание загрузки лого "Яндекс" в шапке')
    def wait_visibility_of_header_logo_yandex(self):
        self.wait_visibility_of_element(MainPageLocators.header_logo_yandex)

    @allure.step('Клик по лого с надписью "Самокат" в шапке')
    def click_on_header_logo_scooter(self):
        self.click_on_element(MainPageLocators.header_logo_scooter)

    @allure.step('Клик по лого "Яндекс" в шапке')
    def click_on_header_logo_yandex(self):
        self.click_on_element(MainPageLocators.header_logo_yandex)

    @allure.step('Ожидание загрузки заголовка главной страницы')
    def wait_visibility_of_main_header(self):
        self.wait_visibility_of_element(MainPageLocators.main_header)

    @allure.step('Проверка отображения заголовка главной страницы')
    def check_displaying_of_main_header(self):
        return self.check_displaying_of_element(MainPageLocators.main_header)

    @allure.step('Скролл до секции "Вопросы о важном"')
    def scroll_to_faq_section(self):
        self.scroll_to_element(MainPageLocators.faq_section)

    @allure.step('Ожидание загрузки нужного номера вопроса в разделе "Вопросы о важнoм"')
    def wait_visibility_of_faq_items(self, data):
        self.wait_visibility_of_element(MainPageLocators.faq_questions_items[data])

    @allure.step('Клик по нужному номеру вопроса в разделе "Вопросы о важнoм"')
    def click_on_faq_items(self, data):
        self.click_on_element(MainPageLocators.faq_questions_items[data])

    @allure.step('Ожидание загрузки нужного номера ответа в разделе "Вопросы о важнoм"')
    def wait_visibility_of_faq_answer(self, data):
        self.wait_visibility_of_element(MainPageLocators.faq_answers_items[data])

    @allure.step('Получение текста нужного номера ответа в разделе "Вопросы о важнoм"')
    def get_displayed_text_from_faq_answer(self, data):
        return self.get_text_on_element(MainPageLocators.faq_answers_items[data])