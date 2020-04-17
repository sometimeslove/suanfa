'''  题目描述
我们提供了一个类：

public class Foo {
  public void one() { print("one"); }
  public void two() { print("two"); }
  public void three() { print("three"); }
}
三个不同的线程将会共用一个 Foo 实例。

线程 A 将会调用 one() 方法
线程 B 将会调用 two() 方法
线程 C 将会调用 three() 方法
请设计修改程序，以确保 two() 方法在 one() 方法之后被执行，three() 方法在 two() 方法之后被执行。

 

示例 1:

输入: [1,2,3]
输出: "onetwothree"
解释:
有三个线程会被异步启动。
输入 [1,2,3] 表示线程 A 将会调用 one() 方法，线程 B 将会调用 two() 方法，线程 C 将会调用 three() 方法。
正确的输出是 "onetwothree"。
示例 2:

输入: [1,3,2]
输出: "onetwothree"
解释:
输入 [1,3,2] 表示线程 A 将会调用 one() 方法，线程 B 将会调用 three() 方法，线程 C 将会调用 two() 方法。
正确的输出是 "onetwothree"。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/print-in-order
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

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
            # 这个time.sleep(0.5)放的位置不同，完全是两种输出，有助于理解整个Condition
            # time.sleep(0.5)
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