import sys
def mySolution(mouse_index,holde_index):
    lenth=len(mouse_index)
    mouse_index.sort()
    holde_index.sort()
    max_time=-sys.maxsize-1
    for i in range(lenth):
        max_time=max(max_time,abs(mouse_index[i]-holde_index[i]))
    return max_time