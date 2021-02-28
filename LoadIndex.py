import requests
import json
import time
import os

def main():
    url = "https://reserve.25team.com/wxappv1/yi/index?version=16"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat",
        "token": os.environ["mytoken"], # "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo2NjQ0MywiZXhwIjoxNzExMzYwNzMwLCJpc3MiOiJnaW4tYmxvZyJ9.hD_uLNUVO0TJNczcwqxb3kBHXk5ywG5MKx4CIuxMv4A",
        "Referer": "https://servicewechat.com/wxd2bebfc67ee4a7eb/73/page-frame.html",
    }
    res_origin = requests.get(url, headers=headers).text
    res = json.loads(res_origin)
    conf = json.dumps(json.loads(res["data"]["conf_titles"]), indent=4, ensure_ascii=False)
    print(conf)
    print()
    res["data"]["conf_titles"] = "Aboved!!!!!!!!!"
    title = "警告!!!!verson不是16" if res["data"]["version"]!=16 else "获取index成功"
    res = json.dumps(res, indent=4, ensure_ascii=False)
    print(res)

    localtime = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()+8*60*60))) # 东八区（Github是UTC）
    serverkey = os.environ["serverkey"]
    url = f"http://sc.ftqq.com/{serverkey}.send"
    data = {
        "text": title + localtime,
        "desp": conf + "\n\r" + res
    }
    requests.post(url, data=data)

    # 更新时强制提醒
    if title != "获取index成功":
        print(14/0)

if __name__ == "__main__":
    main()
