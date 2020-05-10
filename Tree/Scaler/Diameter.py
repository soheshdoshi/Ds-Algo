import sys
def height(node,ans):
    if node is None:
        return 0
    left_h=height(node.left,ans)
    right_h=height(node.rigth,ans)
    ans=max(ans,left_h+right_h+1)
    return 1+max(left_h,right_h)
def diamter(node):
    if node is None:
        return 0
    ans=-sys.maxsize-1
    temp=height(node,ans)
    return ans
