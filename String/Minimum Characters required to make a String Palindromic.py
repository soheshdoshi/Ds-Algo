def checkPalindrom(A):
    if A==A[::-1]:
        #print("inside")
        return True
    return False
def mySolution(A):
    couunt=0
    if checkPalindrom(A):
        return couunt
    for i in A[1:]:
        A=i+A
        print(A)
        couunt+=1
        if checkPalindrom(A):
            return couunt

print(mySolution("babb"))
