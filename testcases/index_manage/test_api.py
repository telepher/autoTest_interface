import allure
import pytest

from common.request_util import RequestUtil
from common.yaml_util import *


@allure.epic('显示管理')
class Test_API:
    base_request = RequestUtil()
    token = ''

    def setup(self):
        print("A")

    def teardown(self):
        print("B")

    # def setup_class(self):
    #     print("数据库操作")
    #
    # def teardown_class(self):
    #     print("数据库关闭")

    @allure.feature('首页')
    def test_index(self, base_url):
        url = str(base_url) + 'api/index/index'
        token = read_yaml('token')
        params = read_yaml('paramsList')[4]
        params['token'] = token
        res = self.base_request.send_Request(url=url, method='POST', params=params)
        self.base_request.assert_response(res, 200, 'success')

    @allure.feature('搜索初始化')
    def test_search_init(self, base_url):
        url = str(base_url) + 'api/search/index'
        token = read_yaml('token')
        params = read_yaml('paramsList')[4]
        params['token'] = token
        data = {
            "wd": "",
            "page": 1,
            "category_id": 0,
            "brand_id": 0
        }
        res = self.base_request.send_Request(url=url, method='POST', params=params, data=data)
        self.base_request.assert_response(res, 200, 'success')

    @pytest.mark.skip('BUG')
    @allure.feature('搜索')
    def test_search_datalist(self, base_url):
        url = str(base_url) + 'api/search/datalist'
        token = read_yaml('token')
        params = read_yaml('paramsList')[4]
        params['token'] = token
        data = {
            "wd": "",
            "page": 1,
            "category_id": 0,
            "brand_id": 0
        }
        res = self.base_request.send_Request(url=url, method='POST', params=params, data=data)
        self.base_request.assert_response(res, 200, 'success')


if __name__ == '__main__':
    Test_API().test_index()
    Test_API().test_search_init()
    Test_API().test_search_datalist()