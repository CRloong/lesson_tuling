'''
利用parse模块模拟post请求
分析百度词典
分析步骤：
1. 打开F12
2. 尝试输入单词
3. 寻找请求地址，确认为http://fanyi.baidu.com/sug
4. 利用NetWork-All-Hearders 查看，发现Formdatad的值是 kw : zhi
5. 检查返回内容格式，发现返回的是json格式内容 ==>>需要用到json包
'''

from urllib import request, parse
#负责处理json格式的模块
import json

'''
大致流程是:
1. 利用data构造内容，然后urlopen打开
2. 返回一个json格式的结果
3. 结果就应该是girl的释义
'''

baseurl = 'http://fanyi.baidu.com/sug'

# 存放用来模拟form的数据一定是dict格式
kw = input("Input english: ")
data = {
    'kw': kw
}

# 需要使用parse模块队data进行编码
data = parse.urlencode(data).encode()

# 构造一个请求头，请求头部应该至少包含传入的数据长度
# request要求传入的请求头是一个dict格式

headers = {
    # 因为使用的是post请求，至少应该包含content - length 字段
    'Content-Length': len(data)
}

# 有了header,data,url,就可以发出请求了

rsp = request.urlopen(baseurl, data=data)

json_data = rsp.read().decode()

print(json_data)

# 把json字符串转化成字典
json_data = json.loads(json_data)
print(json_data)

for item in json_data['data']:
    print(item['k'], "--", item['v'] )