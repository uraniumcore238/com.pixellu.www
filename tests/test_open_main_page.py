from page_objects.MainPageObject import MainPageObject
from utilities.BaseClass import BaseClass


class TestOpenMainPage(BaseClass):

    def test_assert_the_main_page(self):

        mainPageObject = MainPageObject(self.driver)
        mainPageObject.assert_the_header()

