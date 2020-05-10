from Tree import TreeNode
from collections import deque
def rightView(node):
    if node is None:
        return node
    que=deque()
    que.append(node)
    ans=[]
    while que:
        level=[]
        for _ in range(len(que)):
            node=que.popleft()
            level.append(node.val)
            if node.left is not None:
                que.append(node.left)
            if node.right is not None:
                que.append(node.right)
        ans.append(level[-1])
    #print(ans)
    return ans


n=TreeNode.TreeNode(1)
n.left=TreeNode.TreeNode(2)
n.right=TreeNode.TreeNode(3)
n.left.left=TreeNode.TreeNode(4)
n.left.right=TreeNode.TreeNode(5)
n.right.left=TreeNode.TreeNode(6)
n.right.right=TreeNode.TreeNode(7)
n.left.left.left=TreeNode.TreeNode(8)
rightView(n)