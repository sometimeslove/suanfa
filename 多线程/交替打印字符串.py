'''
编写一个可以从 1 到 n 输出代表这个数字的字符串的程序，但是：

如果这个数字可以被 3 整除，输出 "fizz"。
如果这个数字可以被 5 整除，输出 "buzz"。
如果这个数字可以同时被 3 和 5 整除，输出 "fizzbuzz"。
例如，当 n = 15，输出： 1, 2, fizz, 4, buzz, fizz, 7, 8, fizz, buzz, 11, fizz, 13, 14, fizzbuzz。

假设有这么一个类：

class FizzBuzz {
  public FizzBuzz(int n) { ... }               // constructor
  public void fizz(printFizz) { ... }          // only output "fizz"
  public void buzz(printBuzz) { ... }          // only output "buzz"
  public void fizzbuzz(printFizzBuzz) { ... }  // only output "fizzbuzz"
  public void number(printNumber) { ... }      // only output the numbers
}
请你实现一个有四个线程的多线程版  FizzBuzz， 同一个 FizzBuzz 实例会被如下四个线程使用：

线程A将调用 fizz() 来判断是否能被 3 整除，如果可以，则输出 fizz。
线程B将调用 buzz() 来判断是否能被 5 整除，如果可以，则输出 buzz。
线程C将调用 fizzbuzz() 来判断是否同时能被 3 和 5 整除，如果可以，则输出 fizzbuzz。
线程D将调用 number() 来实现输出既不能被 3 整除也不能被 5 整除的数字。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/fizz-buzz-multithreaded
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from threading import Thread, Condition

'''   Condition解法
'''
def fizz():
    while True:
        if con1.acquire():
            con1.wait()
            print('fizz')
            con1.notify()

def buzz():
    while True:
        if con2.acquire():
            con2.wait()
            print('buzz')
            con2.notify()

def fizzbuzz():
    while True:
        if con3.acquire():
            con3.wait()
            print('fizzbuzz')
            con3.notify()

def number():
    while True:
        if con4.acquire():
            con4.wait()
            print(n)
            con4.notify()

con1 = Condition()
con2 = Condition()
con3 = Condition()
con4 = Condition()
n=0

if __name__ == '__main__':
    t1 = Thread(target=fizz)
    t2 = Thread(target=buzz)
    t3 = Thread(target=fizzbuzz)
    t4 = Thread(target=number)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    with con1,con2,con3,con4:
        for i in range(1,16):
            n=i
            if i%3==0 and i%5==0:
                con3.notify()
                con3.wait()
            elif i%3==0:
                con1.notify()
                con1.wait()
            elif i%5==0:
                con2.notify()
                con2.wait()
            else:
                con4.notify()
                con4.wait()

'''  Semaphore解法
def fizz():
    while True:
        if con1.acquire():
            print('fizz')
            con.release()

def buzz():
    while True:
        if con2.acquire():
            print('buzz')
            con.release()

def fizzbuzz():
    while True:
        if con3.acquire():
            print('fizzbuzz')
            con.release()

def number():
    while True:
        if con4.acquire():
            print(n)
            con.release()

con1 = Semaphore(0)
con2 = Semaphore(0)
con3 = Semaphore(0)
con4 = Semaphore(0)
con = Semaphore(1)
n=0

if __name__ == '__main__':

    t1 = Thread(target=fizz)
    t2 = Thread(target=buzz)
    t3 = Thread(target=fizzbuzz)
    t4 = Thread(target=number)
    t1.start()
    t2.start()
    t3.start()
    t4.start()

    for i in range(1,16):
        con.acquire()
        n=i
        if i%3==0 and i%5==0:
            con3.release()
        elif i%3==0:
            con1.release()
        elif i%5==0:
            con2.release()
        else:
            con4.release()
'''

'''  Queue解法
def fizz():
    while True:
        if q1.get():
            print('fizz')
            q.put(1)

def buzz():
    while True:
        if q2.get():
            print('buzz')
            q.put(1)

def fizzbuzz():
    while True:
        if q3.get():
            print('fizzbuzz')
            q.put(1)

def number():
    while True:
        if q4.get():
            print(n)
            q.put(1)

q1 = Queue()
q2 = Queue()
q3 = Queue()
q4 = Queue()
q = Queue()
n=0

if __name__ == '__main__':

    t1 = Thread(target=fizz)
    t2 = Thread(target=buzz)
    t3 = Thread(target=fizzbuzz)
    t4 = Thread(target=number)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    q.put(1)

    for i in range(1,16):
        q.get()
        n=i
        if i%3==0 and i%5==0:
            q3.put(1)
        elif i%3==0:
            q1.put(1)
        elif i%5==0:
            q2.put(1)
        else:
            q4.put(1)
'''