import requests
import json
import time
import random
a=[]
url='https://www.lagou.com/jobs/positionAjax.json?city=%E6%B7%B1%E5%9C%B3&needAddtionalResult=false&isSchoolJob=0'
headers = {
    "Accept-Encoding": 'gzip,deflate,br',
    "Accept-Language": 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    "Content-Type": 'application/x-www-form-urlencoded; charset=UTF-8',
    "Cookie": '_ga=GA1.2.222166711.1519483579; user_trace_token=20180224224621-7a7dde1a-1971-11e8-b08f-5254005c3644; LGUID=20180224224621-7a7de513-1971-11e8-b08f-5254005c3644; index_location_city=%E6%B7%B1%E5%9C%B3; JSESSIONID=ABAAABAAAIAACBIF1852FBC5EBF3DC490D83ACC5D4DBEEB; _gid=GA1.2.1871392688.1519627761; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1519483579,1519486825,1519627761; TG-TRACK-CODE=search_code; LGSID=20180226154155-84e0bb19-1ac8-11e8-b0d9-5254005c3644; X_HTTP_TOKEN=0973826ea19f14e25558620d8818dc19; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; gate_login_token=98b442463eb57cd165345a3836f7944cbde01f5f99c82a02; login=false; unick=""; gate_login_token=""; _putrc=""; _gat=1; LGRID=20180226162517-933d70f8-1ace-11e8-b0d9-5254005c3644; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1519633514; SEARCH_ID=a571bfbd537f4be897dc945982a5e60d',
    # 加入cookie能有效防止反爬取
    "Host": 'www.lagou.com',
    "Origin": 'https://www.lagou.com',
    "Referer": 'https://www.lagou.com/jobs/list_python?labelWords=sug&fromSearch=true&suginput=p',
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36',
}


def lagou_spider(ur, data, head):
    web_data = requests.post(url=ur, data=data, headers=head)  # 定义函数时 参数的对应关系
    info = web_data.json()
    time.sleep(5+random.randint(2, 9))
    result_list = info['content']['positionResult']['result']
    # result_list = info.get('content').get('positionResult').get('result')
    for result in result_list:
        info1 = {
            "companyId": result.get('companyId'),
            "companyFullName ": result.get('companyFullName'),
            "positionName": result.get('positionName'),
            "education": result.get('education'),
            "workYear": result.get('workYear'),
            "salary": result.get('salary')
        }
        a.append(info1)
        print(info1)


data1 = {
        "first": 'true',
        "pn": '1',
        "kd": 'python'
}
lagou_spider(url, data1, headers)
for j in range(2, 14, 1):
    data2 = {
            "first": 'false',
            "pn": '{}'.format(str(j)),
            "kd": 'python'
    }
    lagou_spider(url, data2, headers)
    print(j)
    print('\n=-=-=-=-=-=-=-=-分=-=-=-=-=界-=-=-=-=-\n=-=-=-=线=-=-=-=-=-\n-=-=-=-=-=-=-\n')
for i in a:
    print(i)
