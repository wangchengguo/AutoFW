#coding=utf-8
import requests
import sys
sys.path.append('/home/fzyzgong/project/AutoFWOG/AutoFW/util')
from Mylogging import mylogging

class TestAPI:

    def testDemo(self,protocol,domian,url,headers,param,expected):

        self.protocol = protocol+'://'
        try:
            if param=='' and headers=='':
                r = requests.get(self.protocol + domian + url, timeout=8)
            elif param=='':
                r = requests.get(self.protocol + domian  + url, headers=headers, timeout=8)
            elif headers=='':
                r = requests.get(self.protocol + domian  + url,params=param, timeout=8)
            else:
                r = requests.get(self.protocol + domian  + url,headers=headers, params=param, timeout=8)
            time_consuming = str(r.elapsed.total_seconds())  # 计算接口被调用耗时
            rs = r.json()

            print (rs)
            # 断言 判断接口返回数据是否正常
            if 'resultCode' not in rs.keys():
                print ("AutoFW test reslut:FAILED", str(rs))
            elif rs[expected.keys()[0]] == expected.values()[0]:
                print ('AutoFW test reslut:PASS\'' + "[time_consuming:"+ time_consuming + '] ', str(rs))
            else:
                print ("AutoFW test reslut:FAILED", str(rs))

        except requests.exceptions.ConnectionError:
            mylogging("["+str(__file__)+"]["+self.protocol + domian + url+"]:[requests.exceptions.ConnectionError]")

if __name__ == "__main__":
    protocol = "HTTPS"
    domian = "ta.2boss.cn"
    url = "/rabbit/v1/2bossmoments/count-new"
    headers = {"TBSAccessToken":"2395a9cc328a4091a0c6d25f35178e34"}
    param = 'cityId=605&fromMomentId=388446'
    expected = {"resultCode":0}

    t = TestAPI()
    t.testDemo(protocol,domian,url,headers,param,expected)
