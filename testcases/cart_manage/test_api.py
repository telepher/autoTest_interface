import allure
import pytest

from common.request_util import RequestUtil
from common.yaml_util import *


@allure.epic('购物车管理')
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

    @allure.feature('商品加⼊购物⻋')
    def test_cart_save(self, base_url):
        url = str(base_url) + 'api/cart/save'
        token = read_yaml('token')
        params = read_yaml('paramsList')[4]
        params['token'] = token
        data = {
            "goods_id": "2",
            "spec": [
                {
                    "type": "套餐",
                    "value": "套餐⼆"
                },
                {
                    "type": "颜⾊",
                    "value": "银⾊"
                },
                {
                    "type": "容量",
                    "value": "64G"
                }
            ],
            "stock": 2
        }
        res = self.base_request.send_Request(url=url, method='POST', params=params, data=data)
        self.base_request.assert_response(res, 200, '加入成功')

    @pytest.mark.skip('无权限')
    @allure.feature('购物⻋商品删除')
    def test_cart_delete(self, base_url):
        url = str(base_url) + 'api/cart/delete'
        token = read_yaml('token')
        params = read_yaml('paramsList')[4]
        params['token'] = token
        data = {
            "id": "34,35"
        }
        res = self.base_request.send_Request(url=url, method='POST', params=params, data=data)
        self.base_request.assert_response(res, 200, 'success')

if __name__ == '__main__':
    Test_API().test_cart_save()
    Test_API().test_cart_delete()