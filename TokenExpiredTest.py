import requests
import time

def main():
    url = "https://reserve.25team.com/wxappv1/yi/getUpdateInfo"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat",
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo2NjQ0MywiZXhwIjoxNzExMzYwNzMwLCJpc3MiOiJnaW4tYmxvZyJ9.hD_uLNUVO0TJNczcwqxb3kBHXk5ywG5MKx4CIuxMv4A",
        "Referer": "https://servicewechat.com/wxd2bebfc67ee4a7eb/73/page-frame.html",
    }
    res = requests.get(url, headers=headers)
    print(res.text)

    normal_res = {"code":200,"msg":"ok","data":{"user_id":66443,"role":"student","truename":"胡洪韬","student_id":"2020011610","college_id":8,"college":"信息科学与工程学院","department":"","instructor_id":121,"instructor":"齐待弟","tutor":"","education":"本科","birthplace":"浙江","mobile":"无","create_time":"2020-09-07T10:59:28+08:00"}}
    
    if res.text != normal_res:
        localtime = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        url = f"http://sc.ftqq.com/SCU138613Tf980299c10ed0bc98b9620d68af8f0635fe415a3271b3.send?text=Token有效期监控 {localtime}&desp={res.text}"
        requests.post(url)

if __name__ == "__main__":
    main()
