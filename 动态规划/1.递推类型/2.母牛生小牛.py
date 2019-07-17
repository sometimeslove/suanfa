'''
有一头母牛，它每年年初生一头小母牛。每头小母牛从第四个年头开始，每年年初也生一头小母牛。请编程实现在第n年的时候，共有多少头母牛？
分析：
天数    1   2   3    4      5      6        7
母牛数  1   2   3    4      6      9       13 
表达式  F1  F2  F3  F1+F3  F2+F4  F3+F5   F4+F6
'''

def CountCows(n):
    if n==1:
        return 1
    if n==2:
        return 2
    if n==3:
        return 3
    return CountCows(n-1)+CountCows(n-3)

if __name__ == '__main__':
    print(CountCows(7))
