import threading

from time import sleep


def sing():
    for i in range(3):
        print("唱歌")
        sleep(1)


def dance():
    for i in range(3):
        print("跳舞")
        sleep(1)


# sing()
# dance()
# threads = []
t1 = threading.Thread(target=sing)
t2 = threading.Thread(target=dance)
t1.start()
t2.start()
# threads.append(t1)
# threads.append(t2)
# for t in threads:
#     t.setDaemon(True)
#     t.start()
# t.join(5)

