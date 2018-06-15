'''

使用代理访问网站

'''

from urllib import request,error

if __name__ == "__main__":

    url = "http://www.baidu.com"
    # 1. 设置代理地址
    proxy = {"http": "114.212.12.4:3128"}
    # 2. 创建ProxyHandler
    proxy_handler = request.ProxyHandler(proxy)
    # 3. 创建Opener
    opener = request.build_opener(proxy_handler)
    # 4. 安装Opener
    request.install_opener(opener)

    try:
        rsp = request.urlopen(url)
        html = rsp.read().decode()
        print("8888888"+html)
    except error.HTTPError as e:
        print(e)
    except error.URLError as e:
        print(e)
    except Exception as e:
        print(e)
