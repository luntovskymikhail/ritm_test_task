import allure
from tools.injector import injector
from pages.BasePage import BasePage


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        xpath = self.xpath

        self.page_source = xpath("//body")
        self.elements_btn = xpath("//*[@class='card-body']//*[contains(text(), 'Elements')]")

    @allure.step("Открывает и проверяет главную страницу проекта")
    @injector.inject
    def get_main_page(self):
        with allure.step(f"Переходит на главную страницу {self.base_url}"):
            self.driver.get(self.base_url)

        with allure.step("Проверяет title страницы"):
            self.compare(
                expected="DEMOQA",
                actual=self.driver.title
            )

        with allure.step("Проверяет ссылку страницы"):
            self.compare(
                expected=self.base_url,
                actual=self.driver.current_url
            )

        check_list = ["Elements", "Forms", "Alerts, Frame & Windows", "Widgets",
                      "Interactions", "Book Store Application",
                      "© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED."]

        [self.wait_text(text=i) for i in check_list]

        return self

    @allure.step("Кликает по кнопке 'Elements' и совершает переход")
    def click_elements(self):
        self.wait_appear(self.elements_btn())
        self.elements_btn().click()
        return self
