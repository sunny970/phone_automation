import threading
from time import sleep


class MyThraed1(threading.Thread):
    def __init__(self,num):
        super().__init__()
        self.num = num

    def run(self):
        for i in range(self.num):
            print("唱歌")
            sleep(1)

class MyThraed2(threading.Thread):
    def __init__(self,num):
        super().__init__()
        self.num = num
    def run(self):
        for i in range(self.num):
            print("跳舞")
            sleep(1)

t1 = MyThraed1(4)
t1.start()
t2 = MyThraed2(4)
t2.start()