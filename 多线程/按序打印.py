import time
from threading import  Condition,Thread

con1 = Condition()
con2 = Condition()

def printFirst():
    while True:
        with con1:
            time.sleep(0.5)
            print("first")
            con1.notify_all()
        time.sleep(0.5)

def printSecond():
    while True:
        if con1.acquire():
            con1.wait()
            if con2.acquire():
                print("second")
                con2.notify_all()
                con2.release()
            con1.release()


def printThird():
    while True:
        if con2.acquire():
            con2.wait()
            print("third")
            con2.release()

t1 = Thread(target=printFirst)
t2 = Thread(target=printSecond)
t3 = Thread(target=printThird)
t2.start()
t1.start()
t3.start()