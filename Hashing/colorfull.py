def multi(list):
    ans=1
    for i in list:
        ans*=i
    return ans
def arraySeq(arr_list):
    lenth=len(arr_list)
    s=set()
    for i in range(lenth):
        for j in range(i,lenth):
            k=multi(arr_list[i:j+1])
            if k in s:
                return 0
            else:
                s.add(k)
    return 1


arr=[2,3,4,5]
print(arraySeq(arr))