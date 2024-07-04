import allure
import pytest

from common.request_util import RequestUtil
from common.yaml_util import *


@allure.epic('商品管理')
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

    @allure.feature('商品详情')
    def test_goods_detail(self, base_url):
        url = str(base_url) + 'api/goods/detail'
        token = read_yaml('token')
        params = read_yaml('paramsList')[4]
        params['token'] = token
        data = {
            "goods_id": "12"
        }
        res = self.base_request.send_Request(url=url, method='POST', params=params, data=data)
        self.base_request.assert_response(res, 200, 'success')

    @allure.feature('商品收藏/取消')
    def test_goods_favor(self, base_url):
        url = str(base_url) + 'api/goods/favor'
        token = read_yaml('token')
        params = read_yaml('paramsList')[4]
        params['token'] = token
        data = {
            "id": "12",
            "is_mandatory_favor": "1"
        }
        res = self.base_request.send_Request(url=url, method='POST', params=params, data=data)
        self.base_request.assert_response(res, 200, '收藏成功')

    @pytest.mark.skip('BUG')
    @allure.feature('获取商品规格详情')
    def test_goods_specdetail(self, base_url):
        url = str(base_url) + 'api/goods/specdetail'
        token = read_yaml('token')
        params = read_yaml('paramsList')[4]
        params['token'] = token
        data = {
            "id": "2",
            "spec": [
                {
                    "type": "套餐",
                    "value": "套餐⼆"
                },
                {
                    "type": "颜⾊",
                    "value": "银⾊"},
                {
                    "type": "容量",
                    "value": "64G"
                }
            ],
            "stock": 1
        }
        res = self.base_request.send_Request(url=url, method='POST', params=params, data=data)
        self.base_request.assert_response(res, 200, 'success')

    @pytest.mark.skip('无权限')
    @allure.feature('购买商品数量增加/减少')
    def test_goods_stock(self, base_url):
        url = str(base_url) + 'api/goods/stock'
        token = read_yaml('token')
        params = read_yaml('paramsList')[4]
        params['token'] = token
        data = {
            "id": "2",
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
            "stock": 2}
        res = self.base_request.send_Request(url=url, method='POST', params=params, data=data)
        self.base_request.assert_response(res, 200, 'success')

    @pytest.mark.skip('BUG')
    @allure.feature('获取商品规格类型')
    def test_goods_spectype(self, base_url):
        url = str(base_url) + 'api/goods/spectype'
        token = read_yaml('token')
        params = read_yaml('paramsList')[4]
        params['token'] = token
        data = {
            "id": "2",
            "spec": [
                {
                    "type": "套餐",
                    "value": "套餐⼆"
                }
            ],
            "stock": 2
        }
        res = self.base_request.send_Request(url=url, method='POST', params=params, data=data)
        self.base_request.assert_response(res, 200, 'success')

    @allure.feature('商品浏览历史/⾜迹列表')
    def test_usergoodsfavor_index(self, base_url):
        url = str(base_url) + 'api/usergoodsbrowse/index'
        token = read_yaml('token')
        params = read_yaml('paramsList')[4]
        params['token'] = token
        data = {
            'page': 1
        }
        res = self.base_request.send_Request(url=url, method='POST', params=params, data=data)
        self.base_request.assert_response(res, 200, 'success')

    @pytest.mark.skip('无权限')
    @allure.feature('商品浏览历史/⾜迹删除操作')
    def test_usergoodsfavor_delete(self, base_url):
        url = str(base_url) + 'api/usergoodsbrowse/delete'
        token = read_yaml('token')
        params = read_yaml('paramsList')[4]
        params['token'] = token
        data = {
            "id": "12",
        }
        res = self.base_request.send_Request(url=url, method='POST', params=params, data=data)
        self.base_request.assert_response(res, 200, 'success')

    @allure.feature('商品收藏列表')
    def test_usergoodsfavor_index(self, base_url):
        url = str(base_url) + 'api/usergoodsfavor/index'
        token = read_yaml('token')
        params = read_yaml('paramsList')[4]
        params['token'] = token
        data = {
            'page': 1
        }
        res = self.base_request.send_Request(url=url, method='POST', params=params, data=data)
        self.base_request.assert_response(res, 200, 'success')

    @allure.feature('商品收藏取消操作')
    def test_usergoodsfavor_cancel(self, base_url):
        url = str(base_url) + 'api/usergoodsfavor/cancel'
        token = read_yaml('token')
        params = read_yaml('paramsList')[4]
        params['token'] = token
        data = {
            'id': '12'
        }
        res = self.base_request.send_Request(url=url, method='POST', params=params, data=data)
        self.base_request.assert_response(res, 200, '取消成功')
