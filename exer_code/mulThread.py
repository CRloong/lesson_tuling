
# 多线程测试文档

import time
import threading

def loop1():
    print("Start loop1 at: {}".format(time.ctime()))
    # 睡眠
    time.sleep(2)
    print("End loop1 at: {}".format(time.ctime()))


def loop2():
    print("Start loop2 at: {}".format(time.ctime()))
    # 睡眠
    time.sleep(2)
    print("End loop2 at: {}".format(time.ctime()))


def main():
    print("Start at: {}".format(time.ctime()))
    # 生成实例
    t1 = threading.Thread(target=loop1)
    t1.start()
    t1.join()
    t2 = threading.Thread(target=loop2)
    t2.start()
    t2.join()

    print("All done at：{}".format(time.ctime()))


if __name__ == '__main__':
    main()