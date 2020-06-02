import heapq
import math
def mySolution(A,B):
    total_can=0
    heapq.heapify(A)
    half_candi=0
    while A and A[0]<=B:
        min_pop_ele=heapq.heappop(A)
        half_candi = math.floor(min_pop_ele/2)
        total_can += half_candi
        temp2=0
        if A:
            temp2=heapq.heappop(A)
        else:
            break
        temp2+=(min_pop_ele-(min_pop_ele//2))
        heapq.heappush(A,temp2)
    return total_can


A = [9, 27, 29, 45, 53, 59, 60, 86, 98, 109, 120, 138, 153, 169, 174, 179, 237, 256, 262, 266, 287, 336, 336, 341, 348, 351, 400, 447, 466, 479, 491, 509, 520, 522, 535, 563, 605, 638, 708, 714, 754, 769, 772, 805, 818, 836, 856, 865, 892, 948, 951, 958, 984]
B = 852
print(mySolution(A,B))
