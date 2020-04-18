def mySolution(A):
    A=list(map(float,A))
    lenth=len(A)
    window=[A[0],A[1],A[2]]
    wsum=sum(window)
    if lenth<=3:
        if wsum>1 and wsum<2:
            return 1
        return 0
    for i in range(3,lenth):
        window.sort()
        if wsum>1 and wsum<2:
            return 1
        else:
            if wsum<1:
                wsum-=window[0]
                window[0]=A[i]
                wsum+=window[0]
            else:
                wsum-=window[2]
                window[2]=A[i]
                wsum+=window[2]
    if wsum>1 and wsum<2:
        return 1
    return 0
A= [ "0.503094", "0.648924", "0.999298", "0.853928", "3.457635", "5.030008", "2.434625", "3.081333", "4.629904", "0.551040", "2.950470", "2.248522", "1.426132", "4.848954", "4.624663", "1.095358", "0.980046", "3.620912", "3.504833", "1.930379" ]
print(mySolution(A))
