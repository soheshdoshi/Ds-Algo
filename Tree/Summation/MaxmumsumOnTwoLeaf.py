import sys
def recusiveFunction(node,ans):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return node.val
    left=recusiveFunction(node.left,ans)
    right=recusiveFunction(node.right,ans)
    if node.left is not None and node.right is not None:
        ans[0]=max(ans[0],left+right+node.val)
        return max(left,right)+node.val
    if node.left is None:
        return right+node.val
    if node.right is None:
        return left+node.val
def mySolution(node):
    ans=[-sys.maxsize-1]
    recusiveFunction(node,ans)
    return ans[0]
