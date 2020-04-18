import threading
from time import sleep


class MyThraed1(threading.Thread):
    def run(self):
        for i in range(3):
            print("唱歌")
            sleep(1)

class MyThraed2(threading.Thread):
    def run(self):
        for i in range(3):
            print("跳舞")
            sleep(1)

t1 = MyThraed1()
t1.start()
t2 = MyThraed2()
t2.start()
# 打印所有线程
print(threading.enumerate())
print(threading.active_count())
print(threading.current_thread())
print(threading.main_thread())
