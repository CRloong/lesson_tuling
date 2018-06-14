# 爬虫准备工作
- 参考资料
    - python网络数据采集 * 图灵工业出版社
    - 精通Python爬虫框架Scrapy * 人民邮电出版社
    - [Python3网络爬虫](https://blog.csdn.net/c406495762/article/details/58716886)
- 前置知识
    - url
    - http协议
    - web前段 * html, css, js
    - ajax
    - re,xpath
    - xml
    
# 1.爬虫简介
- 两大特征
    - 能按作者要求下载数据或者内容
    - 能自动在网络上流窜
- 三大步骤
    - 下载网页
    - 提取正确的信息
    - 根据一定规则自动跳到另外的网页上执行上两步内容
  
- 爬虫分类
    - 通用爬虫
    - 专用爬虫（聚焦爬虫）
 
- Python网络包简介
    - Python 2.x: urllib, urllib2, urllib3, httplib, httplib2, requests
    - Python 3.x: urllib, urllib3, httplib2,requests
    
# 2. urllib
- 包含模块
    - urllib.request:打开和读取urls
    - urllib.error: 包含urllib.request产生的常见的错误，使用try捕获
    - urllib.parse: 包含解析url的方法
    - urllib.robotparse: 解析robos.txt文件
    - 案例v01
 
- 网页编码问题解决
    - chardet 可以自动检测页面文件的编码格式，但是可能有误
    - 需要安装，
    - 案v02
- urlopen 的返回对象
    - 案例v03
    - geturl:请求返回对象的url
    - info: 请求返回对象的meta信息
    - getcode: 返回的http code 
- request.data 的使用
    - 访问网络的两种方法
        - get:
            - 利用参数给服务器传递信息
            - 参数为dict，然后需要用parse加密
            - 案例v04
        - post
            - 一般向服务器传递参数使用
            - post是把信息自动加密处理
            - 如果想使用post信息，需要用到data参数
            - 使用post，意味着Http的请求头可能要更改
                - Content-Type: application/x-ww.form-urlencode
                - Content-Length: 数据长度
                - 一旦更改请求方法，请注意其他请求头部信息相应
            - urllib.parse.urlencode可以将字符串自动转成上面的
            - 案例v05