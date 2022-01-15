import requests
from requests import structures
class BaseApi():
    url = ''
    param = {""}
    method = ''
    headers = {}
    datas = ''
    json = {}

    def set_params(self, **param):
        self.parames = param
        return self

    def set_data(self,data):
        self.data = data
        return self

    def set_json(self,json_data):
        self.json = json_data
        return self

    def run(self):
        # verify=False,加上该参数后不会报ssl错误，当为true时默认解析HTTPS内容，但需要添加证书
        #self.response = requests.post(self.url, params=self.parames, headers=self.headers, verify=False, data=self.data,
                                      #json=self.json)
        self.reponse = requests.request(
            self.method,
            self.url,
            params=self.parames,
            headers=self.headers,
            verify=False,
            data=self.data,
            json=self.json
        )

        # print(self.response)
        # 返回类的实例
        return self

    # 断言
    def validate(self, key, expected_value):
        value = self.reponse
        #split切片，取值时不加下标，则切为两个值的数组
        for _key in key.split('.'):
            #print("value--",_key,value,type(value),expected_value)
            #isinstance判断value是否是requests.Response类型
            if isinstance(value,requests.models.Response):
                if _key in ("json()","json"):
                #if _key == "json()":
                    value = self.reponse.json()
                else:
                    #getattr返回value对象中key的属性
                    value = getattr(value,_key)
            #headers.server,在for循环中，第一次循环value为接口整体响应结果获取了headers，
            # 第二次循环value就成了headers的内容，因headers的类型为'requests.structures.CaseInsensitiveDict，
            # 走到了elif中将headers的server值取出来了，继续断言预期结果和取出的值
            elif isinstance(value,(requests.structures.CaseInsensitiveDict,dict)):
                value = value[_key]
            print("value----->", _key, value,type(value))
        # getattr返回对象的某一属性值

        #actual_value = getattr(self.reponse, key)
        assert value == expected_value
        # return self 返回类的实例,多次调用则叠加
        return self