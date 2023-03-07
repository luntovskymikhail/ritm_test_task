from tools.injector import injector
from tools.AllureHelper import AllureHelper
from tools.LocatorHelper import LocatorHelper
from tools.SeleniumHelper import SeleniumHelper


class BasePage:

    @injector.inject
    def __init__(self, driver, settings):
        self.driver = driver

        self.base_url = settings.url

        # упрощаем внешний вид локаторов
        locator = LocatorHelper(driver)
        self.css = locator.css
        self.xpath = locator.xpath
        self.find_id = locator.find_id
        self.name = locator.name
        self.tag = locator.tag
        self.cls_name = locator.class_name
        self.link = locator.link

        # выбрасываем ассерты в allure
        allure_helper = AllureHelper(driver)
        self.compare = allure_helper.compare
        self.difference = allure_helper.difference

        # упрощаем работу с селениумом
        selenium = SeleniumHelper(driver)
        self.scroll = selenium.scroll
        self.switch_window = selenium.switch_window
        self.hover_on = selenium.hover_on
        self.wait_appear = selenium.wait_appear
        self.wait_hide = selenium.wait_hide
        self.wait_text = selenium.wait_text
        self.wait_clickable = selenium.wait_clickable
