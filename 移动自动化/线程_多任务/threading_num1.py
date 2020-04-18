import threading

from time import sleep


def sing(num):
    for i in range(num):
        print("唱歌")
        sleep(1)


def dance(num):
    for i in range(num):
        print("跳舞")
        sleep(1)
# 传参
t1 = threading.Thread(target=sing,args=(5,))
t2 = threading.Thread(target=dance,kwargs={"num":3})
t1.start()
t2.start()