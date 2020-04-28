def mySolution(A):
    s1=[]
    s2=[]
    for i in A:
        if i==')':
            temp=s1.pop()
            while temp!='(':
                s2.append(temp)
                temp=s1.pop()
            if len(s1)>0:
                if s1[-1]=='-':
                    while len(s2)!=0:
                        temp=s2.pop()
                        if temp=='+':
                            s1.append('-')
                        elif temp=='-':
                            s1.append('+')
                        else:
                            s1.append(temp)
            while len(s2)!=0:
                temp=s2.pop()
                s1.append(temp)
        else:
            s1.append(i)
    return s1

def Function(A,B):
    if mySolution(A)==mySolution(B):
        return 1
    return 0


A="-(a+b+c)"
B="-a-b-c"
print(Function(A,B))
