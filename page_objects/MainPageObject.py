import time


class MainPageObject():
    def __init__(self, driver):
        self.driver = driver

    def assert_the_header(self):
        time.sleep(10)