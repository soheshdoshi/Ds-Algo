from collections import  deque
from Tree import TreeNode
def countFullNode(node):
    qur=deque()
    qur.append(node)
    count=0
    while qur:
        node=qur.popleft()
        if node.left is not None and node.right is not None:
            count+=1
        if node.left is not None:
            qur.append(node.left)
        if node.right is not None:
            qur.append(node.right)
    return count

n=TreeNode.TreeNode(20)
n.left=TreeNode.TreeNode(8)
n.right=TreeNode.TreeNode(22)
n.right.left=TreeNode.TreeNode(4)
n.left.left=TreeNode.TreeNode(5)
n.left.right=TreeNode.TreeNode(3)
n.left.right.left=TreeNode.TreeNode(11)
n.left.right.right=TreeNode.TreeNode(14)
n.right.right=TreeNode.TreeNode(25)
print(countFullNode(n))