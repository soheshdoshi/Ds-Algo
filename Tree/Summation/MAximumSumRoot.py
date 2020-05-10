import sys
def recusion(node,ans):
    if node is None:
        ans[0]=0
        return ans
    if node.left is None and node.right is None:
        ans[0]=node.val
        return ans
    left=recusion(node.left,ans)
    right=recusion(node.right,ans)
    if node.left is not None and node.right is not None:
        ans[0]=max(ans[0],left+node.val,right+node.val)

def mySolution(node):
    ans=[-sys.maxsize-1]
    recusion(node,ans)
    return ans[0]




