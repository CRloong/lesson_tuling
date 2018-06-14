from urllib import request
'''
用urllib获取一个网页内容，并打印出来
'''

if __name__ == "__main__":
    url = "http://www.qiongqi.tech/vote.html"
    # 打开相应rul并把相应页面作为返回
    rsp = request.urlopen(url)

    # 把返回的结果读取出来
    # 读取出来内容类型为bytes
    html = rsp.read()
    print(type(html))

    # 如果要把bytes内容换成字符串，需要解码
    html = html.decode()

    print(html)