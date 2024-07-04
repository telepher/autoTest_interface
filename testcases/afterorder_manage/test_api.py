import allure
import pytest

from common.request_util import RequestUtil
from common.yaml_util import *


@allure.epic('售后管理')
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
    @allure.feature('订单售后详情/申请')
    def test_orderaftersale_aftersale(self, base_url):
        url = str(base_url) + 'api/orderaftersale/aftersale'
        token = read_yaml('token')
        params = read_yaml('paramsList')[4]
        params['token'] = token
        data = {
            "oid": "112",
            "did": "124"
        }
        res = self.base_request.send_Request(url=url, method='POST', params=params, data=data)
        self.base_request.assert_response(res, 200, 'success')

    @pytest.mark.skip('无权限')
    @allure.feature('订单售后申请')
    def test_orderaftersale_create(self, base_url):
        url = str(base_url) + 'api/orderaftersale/create'
        token = read_yaml('token')
        params = read_yaml('paramsList')[4]
        params['token'] = token
        data = {
            "order_id": "112",
            "order_detail_id": "124",
            "type": "1",
            "reason": "7天⽆理由退换货",
            "number": "1",
            "price": "0.01",
            "msg": "退款说明⼀下",
        }
        res = self.base_request.send_Request(url=url, method='POST', params=params, data=data)
        self.base_request.assert_response(res, 200, 'success')

    @pytest.mark.skip('无权限')
    @allure.feature('订单售后退货')
    def test_orderaftersale_delivery(self, base_url):
        url = str(base_url) + 'api/orderaftersale/delivery'
        token = read_yaml('token')
        params = read_yaml('paramsList')[4]
        params['token'] = token
        data = {
            "id": "27",
            "express_name": "顺丰快递",
            "express_number": "SY66889988226881"
        }
        res = self.base_request.send_Request(url=url, method='POST', params=params, data=data)
        self.base_request.assert_response(res, 200, 'success')

    @pytest.mark.skip('无权限')
    @allure.feature('订单售后取消')
    def test_orderaftersale_aftersale(self, base_url):
        url = str(base_url) + 'api/orderaftersale/aftersale'
        token = read_yaml('token')
        params = read_yaml('paramsList')[4]
        params['token'] = token
        data = {
            "id": "28"
        }
        res = self.base_request.send_Request(url=url, method='POST', params=params, data=data)
        self.base_request.assert_response(res, 200, 'success')

if __name__ == '__main__':
    Test_API().test_orderaftersale_aftersale()
    Test_API().test_orderaftersale_create()
    Test_API().test_orderaftersale_delivery()
    Test_API().test_orderaftersale_aftersale()