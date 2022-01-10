def test_version():
    from ApiTest import __version__
    assert isinstance(__version__,str)


from Api import BaseApi


#继承base类
class ApiHttpbintestget(BaseApi):
    url = 'https://test-izubackground.izuche.com/izubackground/doLogin.json?username=zhaodongdong'
    param = {"username":"zhaodongdong","password":"12345678","msgcode":"1234"}
    method = 'GET'
    headers = {"CONTENT-TYPE":"application/json"}
    datas = 'abc = 1234'
    json = {'abcd':456}

class ApiHttpbintestpost(BaseApi):
    url = 'https://test-izubackground.izuche.com/izubackground/doLogin.json?username=zhaodongdong'
    param = {"username": "zhaodongdong", "password": "12345678", "msgcode": "1234"}
    method = 'post'
    headers = {"CONTENT-TYPE": "application/json"}
    datas = 'abc = 1234'
    json = {'abcd': 456}
    """def set_params(self,**param):
        self.parames = param
        return self


    def run(self):
        #verify=False,加上该参数后不会报ssl错误
        self.response = requests.post(self.url,params=self.parames,headers=self.headers,verify=False,data=self.data,json=self.json)
        #print(self.response)
        #返回类的实例
        return self

    #断言
    def validate(self,key,expected_value):
        #getattr返回对象的某一属性值
        actual_value = getattr(self.response,key)
        assert actual_value == expected_value
        # return self 返回类的实例,多次调用则叠加
        return self"""

def test_httpbin_get():
    #a = ApiHttpbintestget().set_params(username="zhaodongdong",password=12345678,msgcode=1234)
    #print(a)

    ApiHttpbintestget().set_params(password="12345678",msgcode="1234").set_json({'abcd': 456}) \
        .set_data('abc = 123') \
        .run()\
        .validate("status_code",200)
def test_httpbin_post():
    #a = ApiHttpbintestget().set_params(username="zhaodongdong",password=12345678,msgcode=1234)
    #print(a)


    ApiHttpbintestpost().set_params(password="12345678",msgcode="1234")\
        .set_data('abc = 123')\
        .run()\
        .validate("status_code",200)\
        .validate("headers.Server","nginx")


'''def test_httpbin_post():
    host = 'http://test-izubackground.izuche.com/izubackground/doLogin.json'
    #endpoint = 'post'
    #url = ''.join([host])
    #print('1111%s'%url)
    # data = {'username':'zhaodongdong','password':'12345678','msgcode':'7N3X'}
    #params中内容随URL一并请求服务器，默认放在json?后
    r = requests.post(host,params={"username":'zhaodongdong',"password":"12345678","msgcode":"1234"},headers={"accept":"application/json"})
    print(r.json())
    assert r.status_code == 200
    assert r.headers["Server"] == "nginx"
    assert r.json()['msg'] == "成功"
    assert r.json()['data']['fristLogin'] == 'False'''

#test_httpbin_post()