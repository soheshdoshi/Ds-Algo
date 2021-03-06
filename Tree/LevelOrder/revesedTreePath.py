from collections import defaultdict
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
    print(ans)
    return ans


def revresedTreePath(node,data):
    d=defaultdict()
    stack=[]
    count=0
    while True:
        if node:
            stack.append(node)
            d[count]=node
            count+=1
            node=node.left
        elif stack:
            node=stack.pop()
            if node.val==data:
                start=0
                end=len(d)-1
                while start<end:
                    d[start].val,d[end].val=d[end].val,d[start].val
                    start+=1
                    end-=1
                levelOrder(d[0])
                break
            node=node.right
        else:
            break
    levelOrder(d[0])



n=TreeNode.TreeNode(7)
n.left=TreeNode.TreeNode(6)
n.right=TreeNode.TreeNode(5)
n.left.left=TreeNode.TreeNode(4)
n.left.right=TreeNode.TreeNode(3)
n.right.left=TreeNode.TreeNode(2)
n.right.right=TreeNode.TreeNode(1)
revresedTreePath(n,44)
