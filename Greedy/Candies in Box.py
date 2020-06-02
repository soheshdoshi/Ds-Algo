from heapq import heapify,heappop
import sys
def left_right_arr(arr,lenth):
    temp=[]
    for i in range(0,lenth-1,2):
        temp.append(abs(arr[i]-arr[i+1]))
    return temp

def right_left_arr(arr,lenth):
    temp=[]
    for i in range(lenth-1,0,-2):
        temp.append(abs(arr[i]-arr[i-1]))
    return temp

def mySolution(arr):
    sum1=0
    sum2=0
    lenth=len(arr)
    N=lenth//2
    possible_big_boxes=N-1
    print(possible_big_boxes)
    small_boxes=2*possible_big_boxes



A = [ 81, 19, 42, 70, 79, 56, 38, 106, 59, 47, 16, 65, 93, 34, 112, 37, 57, 29, 114, 107 ]
print(mySolution(A))
