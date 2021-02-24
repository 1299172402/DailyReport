import requests

def main():
    url = "http://tinywebdb.appinventor.space/api?user=dache&secret=a46a5f05&action=update&tag=123&value=748"
    req = requests.post(url)
    print(req)
    print(req.text)

if __name__ == '__main__':
    main()
