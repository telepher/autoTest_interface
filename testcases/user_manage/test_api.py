import allure
import pytest
from jsonpath import jsonpath
from common.request_util import RequestUtil
from common.readExcel import readExcel
from common.yaml_util import *

# loginData = readExcel.excel_to_dict_byName(read_yaml('dataPath'), '账号登录')
loginData = read_testcase(r'D:\Desktop\backp\project\autotest\autoTest_interface\testcases\testData.yaml')
loginData = loginData['datas']


@pytest.mark.run(order=0)
@allure.epic('用户管理')
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

    @allure.feature('登录')
    @pytest.mark.run(order=0)
    @pytest.mark.parametrize('info', loginData)
    def test_login(self, base_url, info):
        url = str(base_url) + info['测试环境']
        res = self.sess.send_Request(url=url, method=info['请求方式'], params=read_yaml('paramsList')[4], data=info['输入数据'])
        datas = {'token': jsonpath(res.json(), '$..token')[0]}
        write_yaml(datas)
        self.sess.assert_response(res, 200, '登录成功')

    @allure.feature('我的留言')
    def test_answer(self, base_url):
        url = str(base_url) + 'api/answer/index'
        token = read_yaml('token')
        params = read_yaml('paramsList')[4]
        params['token'] = token
        res = self.sess.send_Request(url=url, method='POST', params=params, data={"page": 1})
        self.sess.assert_response(res, 200, 'success')

    @allure.feature('留言添加')
    def test_answer_add(self, base_url):
        url = str(base_url) + 'api/answer/add'
        token = read_yaml('token')
        params = read_yaml('paramsList')[4]
        params['token'] = token
        res = self.sess.send_Request(url=url, method='POST', params=params,
                                     data={"name": "龚哥哥", "tel": "13222333322", "content": "hello 你好！"})
        self.sess.assert_response(res, 200, '提交成功')


if __name__ == '__main__':
    Test_API().test_login()
    Test_API().test_answer()
    Test_API().test_answer_add()
