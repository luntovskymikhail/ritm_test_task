import allure
import pytest

from pages.MainPage import MainPage
from pages.elements.ElementsMainPage import ElementsMainPage
from pages.elements.ElementsCheckBoxPage import ElementsCheckBoxPage


@allure.epic("Проверки чекбоксов")
@pytest.mark.checkbox
class TestCheckBox:

    @allure.feature("Проверяет чекбокс в загрузках")
    def test_downloads_checkbox(self, driver, get_main_page):
        MainPage(driver) \
            .click_elements()

        ElementsMainPage(driver) \
            .check_elements_main_page() \
            .click_checkbox()

        ElementsCheckBoxPage(driver) \
            .check_checkbox_page() \
            .expand_home_directory() \
            .expand_downloads_directory() \
            .select_word_file()
