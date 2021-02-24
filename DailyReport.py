import requests

def main():
    url = "https://reserve.25team.com/wxappv1/yi/addReport"

    headers  = {
        'Host':'reserve.25.team',
        'Connection':'keep-alive',
        'Content-Length':'659',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',
        'content-type':'application/json',
        'token':'********',  #需要你自己抓取来使用自己的token
        'referer':'https://servicewechat.com/wxd2bebfc67ee4a7eb/58/page-frame.html',
        'Accept-Encoding':'gzip,deflate,br'
    }

    data = {
        "content": {
            "0": "否",
            "1": "",
            "2": "",
            "3": "",
            "4": "",
            "5": "否",
            "6": "否",
            "7": "否",
            "8": "正常",
            "9": "37.3及以下",
            "10": "浙江省杭州市江干区九和路 经纬度:120.24563937717014,30.30185818142361",
            "11": "否",
            "12": "",
            "13": "",
            "14": "正常（体温37.2及以下）",
            "15": "否",
            "16": ""
        },
        "version": 14,
        "stat_content": {
            "今日是否在京": "否",
            "今日是否在湖北？": "否",
            "今日是否“密切接触”疑似或确诊人群？": "否",
            "今日是否在集中隔离点隔离": "否"
        },
        "location": {
            "province": "浙江省",
            "country": "中国",
            "city": "杭州市",
            "longitude": 120.24563937717014,
            "latitude": 30.30185818142361
        },
        "sick": "正常（体温37.3及以下）",
        "accept_templateid": ""
    }

    res = requests.post(url, headers=headers, json=data)
    print(res.text)

if __name__ == '__main__':
    main()
