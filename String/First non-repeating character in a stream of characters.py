from queue import Queue
def mySolution(arr):
    lenth=len(arr)
    q=Queue()
    charAray=[0]*26
    s=""
    for i in range(lenth):
        q.put(arr[i])
        charAray[ord(arr[i])-ord('a')]+=1
        while not q.empty():
            if charAray[ord(q.queue[0])-ord('a')]>1:
                q.get()
            else:
                s+=q.queue[0]
                break
        if q.empty():
            s+="#"
    return s

arr="abcabc"
print(mySolution(arr))
