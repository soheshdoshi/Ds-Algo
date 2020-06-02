import heapq
import math
def euliq(x1,y1):
    return math.sqrt(pow(x1-0,2)+pow(y1-0,2))

def mySoultion(A,B):
    new_arr=[]
    for i in A:
        heapq.heappush(new_arr,(euliq(i[0],i[1]),i))
    return [heapq.heappop(new_arr)[1] for i in range(B)]
A = [
       [1, 3],
       [-2, 2]
     ]
B = 1
mySoultion(A,B)

