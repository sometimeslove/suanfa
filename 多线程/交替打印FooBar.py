''' 题目概述
我们提供一个类：

class FooBar {
  public void foo() {
    for (int i = 0; i < n; i++) {
      print("foo");
    }
  }

  public void bar() {
    for (int i = 0; i < n; i++) {
      print("bar");
    }
  }
}
两个不同的线程将会共用一个 FooBar 实例。其中一个线程将会调用 foo() 方法，另一个线程将会调用 bar() 方法。

请设计修改程序，以确保 "foobar" 被输出 n 次。
'''
from threading import Condition
from threading import Thread

con1 = Condition()

def foo():
    con1.acquire()
    while True:
        print("foo")
        con1.notify()
        con1.wait()

def bar():
    con1.acquire()
    while True:
        print("bar")
        con1.notify()
        con1.wait()

''' 信号量Semaphore解决生产者消费者问题
con1 = Semaphore(0)
con2 = Semaphore(1)
def foo():
    while True:
        con2.acquire()
        print("foo")
        con1.release()

def bar():
    while True:
        con1.acquire()
        print("bar")
        con2.release()
'''

''' 队列Queue解决生产者消费者问题
q = Queue(1)

def foo():
    while True:
        q.put(1)
        print("foo")

def bar():
    while True:
        q.get()
        print("bar")
'''

t1 = Thread(target=foo)
t2 = Thread(target=bar)
t1.start()
t2.start()