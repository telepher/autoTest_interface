import pytest

from common.yaml_util import *
paramsList = [
    {
        "application": "web",
        "application_client_type": "pc"
    },
    {
        "application": "app",
        "application_client_type": "h5"
    },
    {
        "application": "app",
        "application_client_type": "ios"
    },
    {
        "application": "app",
        "application_client_type": "android"
    },
    {
        "application": "app",
        "application_client_type": "weixin"
    },
    {
        "application": "app",
        "application_client_type": "alipay"
    },
    {
        "application": "app",
        "application_client_type": "baidu"
    },
    {
        "application": "app",
        "application_client_type": "toutiao"
    },
    {
        "application": "app",
        "application_client_type": "qq"
    }
]
dataPath = r'D:\Desktop\backp\project\autoTest\autoTest_interface\datas.xls'

@pytest.fixture(scope='session', autouse=True)
def init():
    # print()
    clear_yaml()
    data = {
        'paramsList': paramsList,
        'dataPath': dataPath
    }
    write_yaml(data)

