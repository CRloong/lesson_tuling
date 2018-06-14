from urllib import request,parse

'''
urlopen返回的内容
'''

if __name__ == "__main__":
    url = "http://www.baidu.com/s?"
    wd = input("Input your keyword:")

    # 想要使用data，需要使用字典结构
    qs = {
        "wd": wd
    }

    # 转换url编码
    qs = parse.urlencode(qs)

    fullurl = url + qs
    print("full url: {}".format(fullurl))

    rsp = request.urlopen(fullurl)

    html = rsp.read()

    html = html.decode()

    print(html)