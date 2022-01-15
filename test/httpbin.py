from ApiTest.Api import BaseApi
#继承base类
class ApiHttpbintestget(BaseApi):
    url = 'https://test-izubackground.izuche.com/izubackground/doLogin.json?username=zhaodongdong'
    param = {"username":"zhaodongdong","password":"12345678","msgcode":"1234"}
    method = 'GET'
    headers = {"CONTENT-TYPE":"application/json"}
    datas = 'abc = 1234'
    #json = {'abcd':456}

class ApiHttpbintestpost(BaseApi):
    url = 'https://test-izubackground.izuche.com/izubackground/doLogin.json?username=zhaodongdong'
    param = {"username": "zhaodongdong", "password": "12345678", "msgcode": "1234"}
    method = 'post'
    headers = {"CONTENT-TYPE": "application/json"}
    datas = 'abc = 1234'
    #json = {'abcd': 456}