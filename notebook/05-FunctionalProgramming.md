# 函数式编程（FunctionalProgramming)
- 基于lambda演算的一种编程方式
    - 程序中只有函数
    - 函数可以作为参数，同样可以作为返回值
    - 纯函数式编程语言: LISP,Haskell
- Python函数式编程知识借鉴函数式编程的一些特点
    - 高阶函数
    - 返回函数 
    - 匿名函数
    - 装饰器
    - 偏函数

## lambda表达式
- 一个表达式，函数体相对简单
- lambda表达式用法
    1. 以lambda开头
    2. 紧跟一定的参数（如果有的话）
    3. 参数后用冒号和表达式主体隔开
    4. 只是一个表达式，所以，没有return

- 计算一个数字的100倍
- stm = lambda x: 100 * x

## 高阶函数
- 把函数作为参数使用的函数，叫高阶函数
    
        def funA():
            print("In funA")
        
        funB = funA