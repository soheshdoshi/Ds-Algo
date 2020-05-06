from Tree import  TreeNode
from collections import defaultdict,deque
def MySoution(node):
    que=deque()
    d=defaultdict(list)
    if node:
        que.append([node,0])
    while que:
        for _ in range(len(que)):
            x,level=que.popleft()
            d[level].append(x.val)
            if x.left:
                que.append([x.left,level+1])
            if x.right:
                que.append([x.right,level+0])
    print(d)





n=TreeNode.TreeNode(8)
n.left=TreeNode.TreeNode(3)
n.right=TreeNode.TreeNode(10)
n.left.left=TreeNode.TreeNode(1)
n.right.left=TreeNode.TreeNode(6)
n.right.left.left=TreeNode.TreeNode(4)
n.right.left.right=TreeNode.TreeNode(7)
n.right.right=TreeNode.TreeNode(14)
n.right.right.left=TreeNode.TreeNode(13)
MySoution((n))
