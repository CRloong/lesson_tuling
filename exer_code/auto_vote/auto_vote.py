
from urllib import request, parse
#负责处理json格式的模块
import json
import random

'''
http://www.qiongqi.tech/vote.html
自动投票
发现其返回的数据结构为
voteList:22,23 目标为23
v:7377  随机4位数字，防止缓存用
请求页面为http://www.qiongqi.tech/vote

大致流程是:
1. 利用data构造内容，然后urlopen打开
2. 返回一个json格式的结果
3. 结果就应该是girl的释义
'''


baseurl = 'http://www.qiongqi.tech/vote'

# 存放用来模拟form的数据一定是dict格式
kw = [22, 23]
data = {
    'voteList': kw,
    'v': random.randint(1001, 9999)
}

print(data)
# 需要使用parse模块队data进行编码
data = parse.urlencode(data).encode()

# 构造一个请求头，请求头部应该至少包含传入的数据长度
# request要求传入的请求头是一个dict格式

headers = {
    # 因为使用的是post请求，至少应该包含content - length 字段
    'Content-Length': len(data)
}
'''
'Host': "www.qiongqi.tech",
'Origin': "http://www.qiongqi.tech",
'Referer': "http://www.qiongqi.tech/vote.html"
'''
# 构造一个Request的实例
req = request.Request(baseurl, data=data, headers=headers)

# 以为已经构造了一个Request的请求实例，则所有的请求信息都可以封装在Request实例中
# 有了header,data,url,就可以发出请求了

rsp = request.urlopen(req)

json_data = rsp.read().decode()

print(json_data)

# 把json字符串转化成字典
json_data = json.loads(json_data)
print(json_data)

'''
for item in json_data['data']:
    print(item['k'], "--", item['v'] )
'''