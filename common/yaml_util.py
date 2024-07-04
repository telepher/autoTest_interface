import os
import yaml
def write_yaml(data):
    with open(r'/testcases/extract.yaml', encoding='utf-8', mode='a+') as f:
        yaml.dump(data, stream=f, allow_unicode=True)


def read_yaml(key):
    with open(r'/testcases/extract.yaml', encoding='utf-8', mode='r') as f:
        value = yaml.load(f, yaml.FullLoader)
        if key in value:
            return value[key]
        else: return '未找到{}'.format(key)


def read_testcase(path):
    with open(path, encoding='utf-8', mode='r') as f:
        value = yaml.load(f, yaml.FullLoader)
        return value


def clear_yaml():
    with open(r'/testcases/extract.yaml', encoding='utf-8', mode='w') as f:
        f.truncate()

# data = read_testcase(r'D:\Desktop\backp\project\autotest\autoTest_interface\testcases\testData.yaml')
# print(data['datas'][0]['测试环境'])
# token = read_yaml('token')
# print(token)
#
# params = data[4]
# params['token'] = token
# print(params)