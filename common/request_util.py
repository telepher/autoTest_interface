import requests
from jsonpath import jsonpath


class RequestUtil(object):
    session = requests.Session()
    def send_Request(self, method, url, params=None, data=None, headers=None):
        res = self.session.request(method, url, params=params, data=data, headers=headers)
        print(res.text)
        return res

    def assert_response(self, response, status_code=200, data=None):
        print(response)
        # 断言响应结果
        assert response.status_code == status_code
        if data is not None:
            assert jsonpath(response.json(), '$..msg')[0] == data


