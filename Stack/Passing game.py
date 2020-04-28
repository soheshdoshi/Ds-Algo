def mySolution(A,B,C):
    stack=[]
    stack.append(B)
    for i in C:
        if i!=0:
            stack.append(i)
        else:
            stack.append(stack[-2])
    return stack.pop()


A = 10
B = 23
C = [ 86,63,60,0,47,0,99,9,0,0 ]


print(mySolution(A,B,C))


