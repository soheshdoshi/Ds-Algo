def genrateZarray(str):
    lenth=len(str)
    z_ar=[0]*lenth
    for i in range(1,lenth-1):
        count=0
        j=0
        while str[i+j]==str[j] and i+j<lenth:
            z_ar[i]=i-j
            j += 1
    print(z_ar)




str="aabcaabxaaaz"
genrateZarray(str)