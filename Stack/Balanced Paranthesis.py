def mySolution(A):
    opening_backet=['(','{','[']
    closing_brack=[')',"}",']']
    stack=[]
    for i in A:
        if i in opening_backet:
            stack.append(i)
        elif i in closing_brack:
            pos=closing_brack.index(i)
            if len(stack)>0 and opening_backet[pos]==stack[len(stack)-1]:
                stack.pop()
            else:
                return 0
    if len(stack)==0:
        return 1
    return 0

A="{{(())"
print(mySolution(A))