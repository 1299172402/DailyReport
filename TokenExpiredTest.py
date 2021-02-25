import requests
import time
import os

def main():
    url = "https://reserve.25team.com/wxappv1/yi/getUpdateInfo"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat",
        "token": os.environ["mytoken"], #"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo2NjQ0MywiZXhwIjoxNzExMzYwNzMwLCJpc3MiOiJnaW4tYmxvZyJ9.hD_uLNUVO0TJNczcwqxb3kBHXk5ywG5MKx4CIuxMv4A",
        "Referer": "https://servicewechat.com/wxd2bebfc67ee4a7eb/73/page-frame.html",
    }
    res = requests.get(url, headers=headers)
    print(res.text)

    localtime = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    url = f"http://sc.ftqq.com/SCU138613Tf980299c10ed0bc98b9620d68af8f0635fe415a3271b3.send?text=Token有效期监控 {localtime}&desp=自2021.02.25 19:00之前获得\n{res.text}"
    requests.post(url)

if __name__ == "__main__":
    main()
