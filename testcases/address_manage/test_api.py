import allure
import pytest

from common.request_util import RequestUtil
from common.yaml_util import *


@allure.epic('地址管理')
class Test_API:
    sess = RequestUtil()

    def setup(self):
        print("A")

    def teardown(self):
        print("B")

    # def setup_class(self):
    #     print("数据库操作")
    #
    # def teardown_class(self):
    #     print("数据库关闭")

    @allure.feature('⾃提地址选择')
    def test_useraddress_extraction(self, base_url):
        url = str(base_url) + 'api/useraddress/extraction'
        token = read_yaml('token')
        params = read_yaml('paramsList')[4]
        params['token'] = token
        res = self.sess.send_Request(url=url, method='POST', params=params)
        self.sess.assert_response(res, 200, '操作成功')

    @allure.feature('地址列表')
    def test_useraddress_index(self, base_url):
        url = str(base_url) + 'api/useraddress/index'
        token = read_yaml('token')
        params = read_yaml('paramsList')[4]
        params['token'] = token
        res = self.sess.send_Request(url=url, method='POST', params=params)
        self.sess.assert_response(res, 200, 'success')

    @allure.feature('地址添加/修改')
    def test_useraddress_save(self, base_url):
        url = str(base_url) + 'api/useraddress/save'
        token = read_yaml('token')
        params = read_yaml('paramsList')[4]
        params['token'] = token
        data = {
            "address": "浦江科技⼴场",
            "alias": "单位",
            "city": "152",
            "county": "1896",
            "id": 0,
            "idcard_back": "https://xxx/1633946364142699.png",
            "idcard_front": "https://xxx/1633946357974689.png",
            "idcard_name": "龚哥哥姓名",
            "idcard_number": "522228666655556666", "is_default": 1,
            "lat": 31.11889286405114,
            "lng": 121.38867189063298,
            "name": "龚哥哥",
            "province": "9",
            "tel": "13222223333"
        }
        res = self.sess.send_Request(url=url, method='POST', params=params, data=data)
        self.sess.assert_response(res, 200, '新增成功')

    @pytest.mark.skip('无权限')
    @allure.feature('设置默认地址')
    def test_useraddress_setdefault(self, base_url):
        url = str(base_url) + 'api/useraddress/setdefault'
        token = read_yaml('token')
        params = read_yaml('paramsList')[4]
        params['token'] = token
        data = {
            'id': '0'
        }
        res = self.sess.send_Request(url=url, method='POST', params=params, data=data)
        self.sess.assert_response(res, 200, 'success')

    @allure.feature('地址详情')
    def test_useraddress_detail(self, base_url):
        url = str(base_url) + 'api/useraddress/detail'
        token = read_yaml('token')
        params = read_yaml('paramsList')[4]
        params['token'] = token
        data = {
            'id': '12'
        }
        res = self.sess.send_Request(url=url, method='POST', params=params, data=data)
        self.sess.assert_response(res, 200, 'success')

if __name__ == '__main__':
    Test_API().test_useraddress_extraction()
    Test_API().test_useraddress_index()
    Test_API().test_useraddress_save()
    Test_API().test_useraddress_setdefault()
    Test_API().test_useraddress_detail()