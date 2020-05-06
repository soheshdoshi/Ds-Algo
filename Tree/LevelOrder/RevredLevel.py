from Tree import TreeNode
from collections import  deque
def reversedLevel(node):
    q=deque()
    ans=[]
    if node:
        q.append(node)
    while q:
        x=q.popleft()
        ans.append(x.val)
        if x.right:
            q.append(x.right)
        if x.left:
            q.append(x.left)
    return ans

n=TreeNode.TreeNode(1)
n.left=TreeNode.TreeNode(2)
n.right=TreeNode.TreeNode(3)
n.left.left=TreeNode.TreeNode(4)
n.left.right=TreeNode.TreeNode(5)
# n.right.left=TreeNode.TreeNode(6)
# n.right.right=TreeNode.TreeNode(7)
print(reversedLevel(n))

