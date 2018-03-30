#coding=utf-8
import requests

class TestAPI:

    def testDemo(self,protocol,domian,url,headers,param,expected):

        self.protocol = protocol+'://'

        if param=='' and headers=='':
            r = requests.get(self.protocol + domian + url, timeout=8)
        elif param=='':
            r = requests.get(self.protocol + domian  + url, headers=headers, timeout=8)
        elif headers=='':
            r = requests.get(self.protocol + domian  + url,params=param, timeout=8)
        else:
            r = requests.get(self.protocol + domian  + url,headers=headers, params=param, timeout=8)

        rs = r.json()

        print (rs)
        # 断言 判断接口返回数据是否正常
        if 'resultCode' not in rs.keys():
            print ("AutoFW test reslut:FAILED", str(rs))
        elif rs[expected.keys()[0]] == expected.values()[0]:
            print ("AutoFW test reslut:PASS", str(rs))
        else:
            print ("AutoFW test reslut:FAILED", str(rs))


if __name__ == "__main__":
    protocol = "HTTP"
    domian = "www.og.demo.com"
    url = "/og/demo"
    headers = {"demo_headers":"demo_headers"}
    param = {"demo_param":"demo_param"}
    expected = {"demo":"Success !"}

    t = TestAPI()
    t.testDemo(protocol,domian,url,headers,param,expected)
