import sys
def mySOlution(node):
    if node is None:
        return 0,-sys.maxsize-1,sys.maxsize,0,True
    if node.left is None and node.right is None:
        return 1,node.val,node.val,1,True

    left=mySOlution(node.left)
    right=mySOlution(node.right)

    res=[0,0,0,0,0]
    res[0]=(1+left[0]+right[0])

    if left[4] and right[4] and left[1]<node.val and right[2]>node.val:
        res[2]=min(left[2],min(left[2],node.val))
        res[1]=max(right[1],max(left[1],node.val))

        res[3]=res[0]
        res[4]=True
        return res
    res[3]=max(left[3],right[3])
    res[4]=False
    return res

