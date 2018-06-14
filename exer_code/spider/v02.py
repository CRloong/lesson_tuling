import urllib
import chardet
'''
使用chardet包自动检测下载页面的编码
'''

if __name__ == "__main__":
    url = "http://www.qiongqi.tech/vote.html"

    rsp = urllib.request.urlopen(url)

    html = rsp.read()

    # 利用 chardet自动检测
    cs = chardet.detect(html)
    print(type(cs))
    print(cs)

    # 使用get取值保证不会出错
    html = html.decode(cs.get("encoding", "utf-8"))
    print(html)