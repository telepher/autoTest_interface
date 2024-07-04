import pytest
import os
# , '-n', '20'
if __name__ == '__main__':
    pytest.main(['-s', '-v', '--capture=sys', '--clean-alluredir', '--alluredir', 'results'])
    os.system('allure generate results -o report -c')