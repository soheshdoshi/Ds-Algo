from collections import Counter


def mySolution(A, B):
    res = []
    dic = {}
    for i in A:
        dic[i] = dic.get(i, 0) + 1

    for i in B:
        if dic.get(i, 0) != 0:
            res = res + [i] * dic[i]
            del dic[i]

    temp = []
    for i in A:
        if dic.get(i, 0) != 0:
            temp.append(i)

    temp.sort()
    res = res + temp
    return res


A = [ 10, 2, 18, 16, 16, 16 ]
B = [ 3, 13, 2, 16, 4, 19 ]
print(mySolution(A,B))