import requests
import time
import os

def main():
    url = "https://reserve.25team.com/wxappv1/yi/getUpdateInfo"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat",
        "token": os.environ["mytoken"],
        "Referer": "https://servicewechat.com/wxd2bebfc67ee4a7eb/73/page-frame.html",
    }
    res = requests.get(url, headers=headers)
    print(res.text)

    localtime = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()+8*60*60))) # 东八区（Github是UTC）
    serverkey = os.environ["serverkey"]
    url = f"http://sc.ftqq.com/{serverkey}.send"
    data = {
        "text": f"Token有效期监控 {localtime}",
        "desp": f"自2021.02.25 19:00之前获得\n\r{res.text}"
    }
    requests.post(url, data=data)

if __name__ == "__main__":
    main()
