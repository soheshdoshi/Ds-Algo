#Given a sorted array of distinct integers A and an integer B, find and return how many rectangles with distinct configurations can be created using elements of this array as length and breadth whose area is lesser than B. (Note that a rectangle of 2 x 3 is different from 3 x 2 if we take configuration into view) For example:
def rectangleCount(arr,area):
    lenth=len(arr)
    count=0
    strat_p=0
    end_p=lenth-1
    while strat_p<=end_p:
        ans=arr[strat_p]*arr[end_p]
        if ans<area:
            count+=2*(end_p-strat_p)+1
            strat_p+=1
        else:
            end_p-=1
    return count%((10**9)+7)
    # for i in range(lenth):
    #     for j in range(lenth):
    #         if arr[i]*arr[j]<area:
    #             count+=1
    #         else:
    #             break
    # return count%((10**9)+7)


A = [1, 2, 3, 4, 5]
B = 5
print(rectangleCount(A,B))