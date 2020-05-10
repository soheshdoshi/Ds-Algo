from Tree import TreeNode
from collections import deque

def mySolution(node):
    que=deque()
    que.append(node)
    odd_sum=0
    even_sum=0
    odd=True
    while que:
        level=0
        for _ in range(len(que)):
            node=que.popleft()
            level+=node.val
            if node.left is not None:
                que.append(node.left)
            if node.right is not None:
                que.append(node.right)
        if odd == True:
            odd=False
            odd_sum+=level
        else:
            even_sum+=level
            odd=True
    return odd_sum-even_sum




n=TreeNode.TreeNode(9)
n.left=TreeNode.TreeNode(2)
n.right=TreeNode.TreeNode(10)
n.left.left=TreeNode.TreeNode(2)
n.left.right=TreeNode.TreeNode(4)
mySolution(n)
