import urllib

'''
urlopen返回的内容
'''

if __name__ == "__main__":
    url = "http://www.qiongqi.tech/vote.html"

    rsp = urllib.request.urlopen(url)

    print(type(rsp))
    print(rsp)
    print("*" * 20)

    print("URL: {0}".format(rsp.geturl()))
    print("info: {}".format(rsp.info))
    print("code: {}".format(rsp.getcode()))

