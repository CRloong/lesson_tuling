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
            - 为了更多的设置请求信息，单纯的通过urlopen函数已经不太好用了
            - 案例v06

- urllib.error
    - URLError产生的原因；
        - 没网
        - 服务器挂接失败
        - 找不到指定服务器
        - 是OSError的子类
   
- ProxyHandler处理（代理服务器）
    - 使用代理IP,
    - 获取代理服务器的地址：
        - www.xicidaili.com
        - www.goubanjia.com
    - 代理用来隐藏真实访问中，代理也不允许频繁访问某一个固定网站，所以，代理一定要很多。
    - 基本使用步骤:
        1. 设置代理地址
        2. 创建ProxyHandler
        3. 创建Opener
        4. 安装Opener    
- 案例v08

- cookie & session
    - http协议是无记忆性的，人们采用的补充协议
    - cookie是发给用户的（即http浏览器）的一段信息，session是保存在服务器上的对应的另一半信息，用来记忆用户信息

- cookie和session的区别
    - 存放位置不同
    - cookie不安全
    - session会保存在服务器上一定时间
    - 单个cookie保存数据不超过4K,很多浏览器限制一个站点最多保存20个
- session的存放位置
    - 存在服务器端
    - 一般情况，session是放在内存中或者数据库中

- 使用cookie登录
    - 直接把cookie复制下来，然后主动放入请求头
    - http模块包含一些关于cookie的模块，通过他们可以自动使用cookie
        - CookieJar
            - 管理存储Cookie，向传出的http请求添加cookie
            - cookie存储在内存中，CookieJar案例回收后cookie将消失
        - FileCookieJar（filename,delayload=None,policy=None)
            - 使用文件管理cookie
            - filename是保存cookie的文件
        - MozillaCookieJar（filename,delayload=None,policy=None)
            - 创建与mozilla浏览器的cookie.txt兼容的FileCookieJar实例
        - LwpCookieJar（filename,delayload=None,policy=None)
            - - 创建与libwww-per标准兼容的Set-Cookie3兼容的FileCookieJar实例
        - 关系：CookieJar-->FileCookieJar-->MozillaCookieJar & LwpCookieJar
        -               