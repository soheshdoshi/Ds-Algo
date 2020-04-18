from collections import  Counter
def CountOaArray(arr):
    d=Counter(arr)
    return d
def CountPair(arr,fsum):
    counter_dict=CountOaArray(arr)
    #print(counter_dict)
    arr=list(counter_dict.keys())
    #print(arr)
    lenth = len(arr)
    strat_p=0
    end_p=lenth-1
    count=0
    while strat_p<end_p:
        ans=arr[strat_p]+arr[end_p]
        if ans==fsum:
            count+=max(counter_dict[arr[strat_p]],counter_dict[arr[end_p]])
            #print(count)
            strat_p+=1
            end_p-=1
        elif ans<fsum:
            strat_p+=1
        elif ans>fsum:
            end_p-=1
    return count%((10**9)+7)
A = [ 1, 2, 6, 6, 7, 9, 9 ]
B = 13
print(CountPair(A,B))