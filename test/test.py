import requests
from requests import structures

#在obj中遍历传入attrspec的属性值
def resolve(obj, attrspec):
    for attr in attrspec.split("."):
        try:
            obj = obj[attr]
        except (TypeError, KeyError):
            obj = getattr(obj, attr)
    return obj
def test_httpbin_post():
    host = 'http://test-izubackground.izuche.com/izubackground/doLogin.json'
    #endpoint = 'post'
    #url = ''.join([host])
    #print('1111%s'%url)
    # data = {'username':'zhaodongdong','password':'12345678','msgcode':'7N3X'}
    #params中内容随URL一并请求服务器，默认放在json?后
    value = requests.post(host,params={"username":'zhaodongdong',"password":"12345678","msgcode":"1234"},headers={"accept":"application/json"})
    #response = requests.request(value)
    print(value.json())
    a = resolve(value.json(),'data.Authorization')
    #sid = getattr(value.json(),'[msg]')
    print(a)