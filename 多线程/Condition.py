# encoding: UTF-8
import threading
import time

# 商品
product = None
# 条件变量
con = threading.Condition()

# 生产者方法
def produce():
    global product

    if con.acquire():
        while True:
            if product is None:
                print ('produce...')
                product = 'anything'

                # 通知消费者，商品已经生产
                con.notify()

            # 等待通知
            con.wait()
            time.sleep(2)

# 消费者方法
def consume():
    global product

    if con.acquire():
        while True:
            if product is not None:
                print ('consume...')
                product = None

                # 通知生产者，商品已经没了
                con.notify()

            # 等待通知
            con.wait()
            time.sleep(2)

t1 = threading.Thread(target=produce)
t2 = threading.Thread(target=consume)
t2.start()
t1.start()



# import threading
#
# def grilfriend():
#     with cond:  # 上第一层锁
#         print("女：随便。")
#         cond.notify()
#
#         cond.wait()
#         print("女：油腻了啦！")
#         cond.notify()
#
#         cond.wait()
#         print("女：会不会清淡了？")
#         cond.notify()
#
#         cond.wait()
#         print("女：随便。")
#
# def boyfriend():
#     with cond:
#         print("男：今天吃什么？")
#         cond.notify()
#
#         cond.wait()
#         print("男：五花肉好不好？")
#         cond.notify()
#
#         cond.wait()
#         print("男：水煮西兰花呢？")
#         cond.notify()
#
#         cond.wait()
#         print("男：那你想吃什么？")
#         cond.notify()
#
# if __name__ == "__main__":
#     cond = threading.Condition()
#
#     bthread = threading.Thread(target=boyfriend)
#     gthread = threading.Thread(target=grilfriend)
#
#     bthread.start() # 为让 男友 先说话，所以先执行boyfriend的线程
#     gthread.start()