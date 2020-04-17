'''
假设有这么一个类：

class ZeroEvenOdd {
  public ZeroEvenOdd(int n) { ... }      // 构造函数
  public void zero(printNumber) { ... }  // 仅打印出 0
  public void even(printNumber) { ... }  // 仅打印出 偶数
  public void odd(printNumber) { ... }   // 仅打印出 奇数
}
相同的一个 ZeroEvenOdd 类实例将会传递给三个不同的线程：

线程 A 将调用 zero()，它只输出 0 。
线程 B 将调用 even()，它只输出偶数。
线程 C 将调用 odd()，它只输出奇数。
每个线程都有一个 printNumber 方法来输出一个整数。请修改给出的代码以输出整数序列 010203040506... ，其中序列的长度必须为 2n。

示例 1：

输入：n = 2
输出："0102"
说明：三条线程异步执行，其中一个调用 zero()，另一个线程调用 even()，最后一个线程调用odd()。正确的输出为 "0102"。
示例 2：

输入：n = 5
输出："0102030405"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/print-zero-even-odd
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from threading import Condition
from threading import Thread

con1 = Condition()
con2 = Condition()
n=0

def zero():
    con1.acquire()
    con2.acquire()
    while True:
        print("0")
        con1.notify()
        con1.wait()
        print("0")
        con2.notify()
        con2.wait()

def odd():
    global n
    con1.acquire()
    while True:
        n+=1
        print(n)
        con1.notify()
        con1.wait()

def even():
    global n
    con2.acquire()
    while True:
        n+=1
        print(n)
        con2.notify()
        con2.wait()

'''  信号量方法
semzero  = Semaphore(1)
semodd = Semaphore(0)
semeven = Semaphore(0)
n=1

def zero():
    while True:
        semzero.acquire()
        print('0')
        if n%2 == 1:
            semodd.release()
        else:
            semeven.release()

def odd():
    global n
    while n>0:
        semodd.acquire()
        if n%2 == 1:
            print(n)
            n+=1
        semzero.release()



def even():
    global n
    while n>0:
        semeven.acquire()
        if n%2 == 0:
            print(n)
            n+=1
        semzero.release()
'''
''' 队列方法
qzero  = Queue()
qodd = Queue()
qeven = Queue()

n=1

def zero():
    qzero.put(n)
    while True:
        tmp = qzero.get()
        print('0')
        if tmp%2 == 1:
            qodd.put(tmp)
        else:
            qeven.put(tmp)

def odd():
    while n>0:
        tmp = qodd.get()
        print(tmp)
        tmp+=1
        qzero.put(tmp)

def even():
    while n>0:
        tmp = qeven.get()
        print(tmp)
        tmp+=1
        qzero.put(tmp)
'''



t1 = Thread(target=zero,name='T-Zero')
t2 = Thread(target=odd,name='T-Odd')
t3 = Thread(target=even,name='T-Even')

t1.start()
t2.start()
t3.start()