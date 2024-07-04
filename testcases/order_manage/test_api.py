import allure
import pytest

from common.readExcel import readExcel
from common.request_util import RequestUtil
from common.yaml_util import *


@allure.epic('订单管理')
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

    def test_order_index(self, base_url):
        url = str(base_url) + 'api/order/index'
        token = read_yaml('token')
        params = read_yaml('paramsList')[4]
        params['token'] = token
        data = {
            "page": 1,
            "keywords": "",
            "status": "-1",
            "is_more": 1
        }
        res = self.base_request.send_Request(url=url, method='POST', params=params, data=data)
        self.base_request.assert_response(res, 200, 'success')

    @pytest.mark.skip(reason='没后台权限')
    def test_order_detail(self, base_url):
        url = str(base_url) + 'api/order/detail'
        token = read_yaml('token')
        params = read_yaml('paramsList')[4]
        params['token'] = token
        data = {
            'id': '12'
        }
        res = self.base_request.send_Request(url=url, method='POST', params=params, data=data)
        self.base_request.assert_response(res, 200, 'success')

    @pytest.mark.skip(reason='没后台权限')
    def test_order_cancel(self, base_url):
        url = str(base_url) + 'api/order/cancel'
        token = read_yaml('token')
        params = read_yaml('paramsList')[4]
        params['token'] = token
        data = {
            'id': '12'
        }
        res = self.base_request.send_Request(url=url, method='POST', params=params, data=data)
        self.base_request.assert_response(res, 200, '取消成功')

    @pytest.mark.skip(reason='没后台权限')
    def test_order_buy(self, base_url):
        url = str(base_url) + 'api/buy/index'
        token = read_yaml('token')
        params = read_yaml('paramsList')[4]
        params['token'] = token
        data = {
            "buy_type": "cart",
            "ids": "189",
            "address_id": 0,
            "payment_id": 0,
            "site_model": 0,
            "is_points": 0
        }
        res = self.base_request.send_Request(url=url, method='POST', params=params, data=data)
        self.base_request.assert_response(res, 200, 'success')

    @pytest.mark.skip(reason='没后台权限')
    def test_order_collect(self, base_url):
        url = str(base_url) + 'api/order/collect'
        token = read_yaml('token')
        params = read_yaml('paramsList')[4]
        params['token'] = token
        data = {
            'id': '12'
        }
        res = self.base_request.send_Request(url=url, method='POST', params=params, data=data)
        self.base_request.assert_response(res, 200, '收货成功')

    @pytest.mark.skip(reason='没后台权限')
    def test_order_pay(self, base_url):
        url = str(base_url) + 'api/order/pay'
        token = read_yaml('token')
        params = read_yaml('paramsList')[4]
        params['token'] = token
        data = {
            "ids": "110",
            "payment_id": "13"
        }
        res = self.base_request.send_Request(url=url, method='POST', params=params, data=data)
        self.base_request.assert_response(res, 200, 'success')

    @pytest.mark.skip(reason='没后台权限')
    def test_order_delete(self, base_url):
        url = str(base_url) + 'api/order/delete'
        token = read_yaml('token')
        params = read_yaml('paramsList')[4]
        params['token'] = token
        data = {
            'id': '12'
        }
        res = self.base_request.send_Request(url=url, method='POST', params=params, data=data)
        self.base_request.assert_response(res, 200, '删除成功')

    @pytest.mark.skip(reason='没后台权限')
    def test_order_commentssave(self, base_url):
        url = str(base_url) + 'api/order/commentssave'
        token = read_yaml('token')
        params = read_yaml('paramsList')[4]
        params['token'] = token
        data = {
            "is_anonymous": "0",
            "id": "113",
            "goods_id": "[12]",
            "rating": "[5]",
            "content": "['宝⻉⾮常好！']",
        }
        res = self.base_request.send_Request(url=url, method='POST', params=params, data=data)
        self.base_request.assert_response(res, 200, '评论成功')

if __name__ == '__main__':
    Test_API().test_order_index()
