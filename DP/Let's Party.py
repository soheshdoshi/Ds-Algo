mod=10003

def mySolution(A):
    if A==1:
        return 1
    elif A==2:
        return 2
    else:
        f=1
        s=2
        for i in range(3,A+1):
            t=((s%mod)+(f%mod*(i-1)%mod)%mod)%mod
            print(t)
            f=s
            s=t
        return t
        ways=[0]*(A+1)
        way=1
        ways[2]=2
        for i in range(3,A+1):
            f=(ways[i-1]%mod*1)
            s=(ways[i-2]%mod*(i-1)%mod)%mod
            ways[i]=(f%mod+s%mod)%mod
        return ways


print(mySolution(17))
