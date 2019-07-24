def one_zero_bag(w,v,c):
    length = len(w)
    cost = [ [0 for j in range(c)]  for i in range(length+1)]
    index = []
    for i in range(length):
        for j in range(1,c):
            if j>=w[i]:
                cost[i+1][j] = cost[i][j-w[i]]+v[i] if (cost[i][j-w[i]]+v[i])>cost[i][j] else cost[i][j]
            else:
                cost[i+1][j] =cost[i][j]
    return cost
def getIndex (arr,w,c):
    index =[]
    c=c-1
    length = len(w)
    for i in range(length,0,-1):
        if arr[i][c]!=arr[i-1][c]:
            index.append(i-1)
            c = c-w[i-1]
    return index

if __name__ == '__main__':
    w=[2,2,6,5,4]
    v=[6,3,5,4,6]
    c=10
    arr = one_zero_bag(w,v,c)
    print(arr)
    print(arr[-1][-1])
    print(getIndex(arr,w,c))
