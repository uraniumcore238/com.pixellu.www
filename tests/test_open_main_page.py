import allure

from page_objects.MainPageObject import MainPageObject
from utilities.BaseClass import BaseClass


class TestOpenMainPage(BaseClass):

    @allure.feature('Аллюр фича')
    @allure.story('Аллюр стори')
    @allure.severity('critical')
    def test_assert_the_main_page(self):

        with allure.step('Open main page'):
            mainPageObject = MainPageObject(self.driver)
            mainPageObject.assert_the_header()
            print('Page was successfully opened')

