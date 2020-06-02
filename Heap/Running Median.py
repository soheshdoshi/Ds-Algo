import heapq
def addNum(num,lower,higher):
    if not lower or num<-lower[0]:
        heapq.heappush(lower,-num)
    else:
        heapq.heappush(higher,num)
def rebalance(lower,higer):
    if len(lower)-len(higer)>=2:
        heapq.heappush(higer,-heapq.heappop(lower))
    elif len(higer)-len(lower)>=2:
        heapq.heappush(lower,-heapq.heappop(higer))
def getMedian(lowers, highers):
    if len(lowers)>=len(highers):
        return -lowers[0]
    else:
        return highers[0]
def mySolution(arr):
    lower=[]
    higer=[]
    result=[]
    for i in arr:
        addNum(i,lower,higer)
        rebalance(lower,higer)
        #print(lower,higer)
        result.append(round(getMedian(lower, higer), 1))
    return result

A = [5, 17, 100, 11]
mySolution(A)