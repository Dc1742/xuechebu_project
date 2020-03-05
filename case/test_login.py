import time

import pytest

from utils import get_driver


class TestLogin(object):
    @pytest.fixture()
    def before_func(self):
        self.driver=get_driver()

        yield
        time.sleep(2)
        self.driver.quit()
    def test_login(self,before_func):
        pass