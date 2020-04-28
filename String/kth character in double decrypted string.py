def mySolution(s,k):
    lenth=len(s)
    l=[]
    index=0
    i=0
    while i<lenth:
        if s[i].isalpha():
            index+=1
            l.append([s[i],index])
            i+=1
        elif s[i].isdigit():
            ans=0
            while i<lenth and s[i].isdigit():
                ans=ans*10+int(s[i])
                i+=1
            index*=ans
        if index>k:
            break
    while l:
        first,second=l[-1]
        k=k%second
        if k==0:
            return first
        l.pop()

A="tu16mj75s"
B=56
print(mySolution(A,B))





