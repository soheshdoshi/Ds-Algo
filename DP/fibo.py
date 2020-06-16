def mySolution(nth):
    if nth == 0:
        return 0
    elif nth ==1:
        return 1
    else:
        total = [0]*(nth+1)
        total[0]=0
        total[1]=1
        for i in range(2,nth+1):
            total[i]=total[i-1]+total[i-2]
        return total[-1]

print(mySolution(3))