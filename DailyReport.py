import requests
import os
import time

def main():
    url = "https://reserve.25team.com/wxappv1/yi/addReport"
    headers  = {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat",
        "token": os.environ["mytoken"], #"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo2NjQ0MywiZXhwIjoxNzExMzYwNzMwLCJpc3MiOiJnaW4tYmxvZyJ9.hD_uLNUVO0TJNczcwqxb3kBHXk5ywG5MKx4CIuxMv4A",  #自己的token
        "referer":"https://servicewechat.com/wxd2bebfc67ee4a7eb/73/page-frame.html",
    }
    data = {"content":{"0":"否","1":"","2":"","3":"","4":"","5":"低风险","6":"浙江省杭州市拱墅区莫干山路 经纬度:120.15515,30.27415","7":"正常","8":"37.3以下","9":"绿色","10":"均正常","11":"无","12":"否","13":"","14":""},"version":16,"stat_content":{},"location":{"province":"浙江省","country":"中国","city":"杭州市","longitude":120.15515,"latitude":30.27415},"sick":"","accept_templateid":""}
    res = requests.post(url, headers=headers, json=data)
    print(res.text)
    
    localtime = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    serverkey = os.environ["serverkey"]
    serverkey_turbo = os.environ["serverkey_turbo"]
    scurl = f"http://sc.ftqq.com/{serverkey}.send?text=上报结果 {localtime}&desp={res.text}"
    scturl = f"https://sctapi.ftqq.com/{serverkey_turbo}.send?title=上报结果 {localtime}   {res.text}"
    requests.post(scurl)
    requests.post(scturl)

if __name__ == "__main__":
    main()
