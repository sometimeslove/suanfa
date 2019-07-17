'''
子串（Substring）是串的一个连续的部分，子序列（Subsequence）则是从不改变序列的顺序，而从序列中去掉任意的元素而获得的新序列；
更简略地说，
前者（子串）的字符的位置必须连续，后者（子序列LCS）则不必。比如字符串acdfg同akdfc的最长公共子串为df，而他们的最长公共子序列是adf。
'''

import  numpy as np
def lcseq(str1,str2):
    len1,len2 = len(str1),len(str2)
    # 创建数组用来存放长度
    value = np.zeros((len2+1)*(len1+1)).reshape((len2+1),(len1+1))
    # 创建数组用来存放索引
    seq = np.zeros((len2+1)*(len1+1)).reshape((len2+1),(len1+1))-1
    for i in range(1,len2+1):
        for j in range(1,len1+1):
            if str2[i-1] == str1[j-1]:
                value[i,j] = value[i-1,j-1] +1
                seq[i,j] = i-1
            elif value[i-1,j]>value[i,j-1]:
                value[i,j] = value[i-1,j]
                seq[i,j] = seq[i-1,j]
            else:
                value[i,j] = value[i,j-1]
                seq[i,j] = seq[i,j-1]
    print(value,)
    print(seq,)

if __name__ == '__main__':
    lcseq('reawq','werfegq')