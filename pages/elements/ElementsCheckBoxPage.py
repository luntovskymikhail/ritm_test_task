import allure
from pages.elements.ElementsMainPage import ElementsMainPage


class ElementsCheckBoxPage(ElementsMainPage):

    def __init__(self, driver):
        super().__init__(driver)

        self.checkbox_url = f"{self.base_url}checkbox"

        xpath = self.xpath
        find_id = self.find_id

        self.home_directory_btn = xpath("//button[@title='Toggle']")

        # знаю что это плохой локатор
        self.downloads_btn = xpath("//*[@id='tree-node']/ol/li/ol/li[3]/span/button")

        self.word_file_btn = xpath("//span[contains(text(), 'Word File.doc')]")

        self.success_msg = find_id("result")

    @allure.step("Проверяет что мы на странице 'Elements'")
    def check_checkbox_page(self):
        with allure.step("Проверяет title страницы"):
            self.compare(
                expected="DEMOQA",
                actual=self.driver.title
            )

        with allure.step("Проверяет ссылку страницы"):
            self.compare(
                expected=self.checkbox_url,
                actual=self.driver.current_url
            )

        self.wait_text(text="Home")

        return self

    @allure.step("Раскрывает директорию 'Home'")
    def expand_home_directory(self):
        self.wait_appear(self.home_directory_btn())
        self.home_directory_btn().click()
        return self

    @allure.step("Раскрывает директорию 'Downloads'")
    def expand_downloads_directory(self):
        self.wait_appear(self.downloads_btn())
        self.downloads_btn().click()
        return self

    def select_word_file(self):
        with allure.step("Выбирает Word File.doc"):
            self.wait_appear(self.word_file_btn())
            self.word_file_btn().click()

        with allure.step("Проверяет что Word File выбран"):
            self.compare(
                expected="You have selected :\nwordFile",
                actual=self.success_msg().text
            )
