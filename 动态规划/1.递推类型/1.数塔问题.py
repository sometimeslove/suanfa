
'''
有如下所示的数塔，要求从顶层走到底层，若每一步只能走到相邻的结点，则经过的结点的数字之和最大是多少？
input
输入数据首先包括一个整数C,表示测试实例的个数，每个测试实例的第一行是一个整数N(1 <= N <= 100)，表示数塔的高度，
接下来用N行数字表示数塔，其中第i行有个i个整数，且所有的整数均在区间[0,99]内。
output
对于每个测试实例，输出可能得到的最大和，每个实例的输出占一行。
题目链接：http://acm.hdu.edu.cn/showproblem.php?pid=2084
'''
import  random
def makeArr(height):
    arr = [[random.randint(0,10) if j<=i else float("-inf") for j in range(height)] for  i in range(height)]
    return arr

def maxSum(arr):
    length = len(arr)
    tmpvalue = [[float("-inf") for i in range(length)] for j in range(length)]
    tmpindex = [[-1 for i in range(length)] for  j in range(length)]
    tmpvalue[0] = arr[0]
    for i in range(1,length):
        for j in range(0,i+1):
            if j==0 :
                tmpvalue[i][j] = tmpvalue[i - 1][j] + arr[i][j]
                tmpindex[i][j] = j;
            else:
                tmpvalue[i][j] = tmpvalue[i - 1][j] + arr[i][j]
                tmpindex[i][j] = j;
                if tmpvalue[i][j]<tmpvalue[i - 1][j-1] + arr[i][j]:
                    tmpvalue[i][j] = tmpvalue[i - 1][j-1] + arr[i][j]
                    tmpindex[i][j] = j-1;
    return tmpvalue,tmpindex

def getMax(tmpvalue,tmpindex):
    length =len(tmpvalue)
    maxvalue = max(tmpvalue[-1])
    tmp = tmpvalue[-1].index(maxvalue)
    list = [[length-1,tmp]]
    for i in range(length-2,0,-1):
        list.append([i,tmpindex[i+1][tmp]])
        tmp=tmpindex[i+1][tmp]
    list.append((0,0))
    return maxvalue,list

if __name__ == '__main__':
    arr = makeArr(4)
    val,index = maxSum(arr)
    print(arr)
    print(val)
    print(index)
    print(getMax(val,index))
