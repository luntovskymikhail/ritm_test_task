import allure
from pages.MainPage import MainPage


class ElementsMainPage(MainPage):

    def __init__(self, driver):
        super().__init__(driver)

        self.elements_url = f"{self.base_url}elements"

        xpath = self.xpath

        self.checkbox_btn = xpath("//span[contains(text(), 'Check Box')]")

    @allure.step("Проверяет что мы на странице 'Elements'")
    def check_elements_main_page(self):
        with allure.step("Проверяет title страницы"):
            self.compare(
                expected="DEMOQA",
                actual=self.driver.title
            )

        with allure.step("Проверяет ссылку страницы"):
            self.compare(
                expected=self.elements_url,
                actual=self.driver.current_url
            )

        check_list = ["Elements", "Text Box", "Check Box", "Radio Button", "Web Tables",
                      "Buttons", "Links", "Broken Links - Images", "Upload and Download",
                      "Dynamic Properties", "Forms", "Alerts, Frame & Windows", "Widgets",
                      "Interactions", "Book Store Application",
                      "Please select an item from left to start practice.",
                      "© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED."]

        [self.wait_text(text=i) for i in check_list]

        return self

    @allure.step("Кликает в боковом меню по 'Checkbox'")
    def click_checkbox(self):
        self.wait_appear(self.checkbox_btn())
        self.checkbox_btn().click()
        return self
