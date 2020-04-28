def expresion(op1,op2,op):
    if op=='+':
        return op1+op2
    elif op=='-':
        return op1-op2
    elif op=='/':
        return op1//op2
    elif op=='*':
        return op1*op2
def mySolution(A):
    stack=[]
    for i in A:
        if i in ['+','-','*','/']:
            op2=int(stack.pop())
            op1=int(stack.pop())
            stack.append(expresion(op1,op2,i))
        else:
            stack.append(i)
    return stack[-1]


A = ["4", "13", "5", "/", "+"]
print(mySolution(A))