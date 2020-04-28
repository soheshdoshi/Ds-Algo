from collections import deque
def maxXOR(arr):
    stack = deque()
    l = 0
    res1 = 0
    for i in arr:
        while stack and stack[-1] < i:
            stack.pop()
            l -= 1
        stack.append(i)
        l += 1
        if l > 1:
            res1 = max(res1, stack[-1] ^ stack[-2])
    res2 = 0
    stack.clear()
    l = 0
    arr.reverse()
    for i in arr:
        while stack and stack[-1] < i:
            stack.pop()
            l -= 1
        stack.append(i)
        l += 1
        if l > 1:
            res2 = max(res2, stack[-1] ^ stack[-2])
    return max(res1, res2)

A =[ 9, 8, 3, 5, 7 ]
print(mySolution(A))