import pytest

if __name__ == '__main__':
    # import os
    # pytest.main(['-m P1', '--alluredir=alluredir/'])
    # allure generate --clean ./alluredir -o ./allure-report/html
    # os.popen("allure serve ./alluredir")
    pytest.main([
        '-m P1',
        '--report=a_demo.html',
        '--title=一个demo',
        '--tester=zhenzhu',
        '--desc=一个demo',
        '--template=1'
    ])


