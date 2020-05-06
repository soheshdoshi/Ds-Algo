from Tree import TreeNode
from collections import deque
def levelOrder(node):
    que=deque()
    que.append(node)
    ans=[]
    while len(que):
        level=[]
        for _ in range(len(que)):
            x=que.popleft()
            level.append(x.val)
            if x.left is not None:
                que.append(x.left)
            if x.right is not None:
                que.append(x.right)
        ans.append(level)
    return ans





n=TreeNode.TreeNode(1)
n.left=TreeNode.TreeNode(2)
n.right=TreeNode.TreeNode(3)
n.left.left=TreeNode.TreeNode(4)
n.left.right=TreeNode.TreeNode(5)
n.right.left=TreeNode.TreeNode(6)
n.right.right=TreeNode.TreeNode(7)
print(levelOrder(n))