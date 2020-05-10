from Tree import TreeNode

def leftNode(node,ans):
    if node is None:
        return ans
    else:
        ans.append(node.val)
        leftNode(node.left,ans)
        return ans


def rigthNode(node,ans):
    if node is None:
        return ans
    else:
        ans.append(node.val)
        rigthNode(node.right,ans)
        return ans

from collections import deque
def Topview(node):
    if node is None:
        return node
    que=deque()
    que.append(node)
    parent=[]
    left=[]
    right=[]
    while que:
        level=[]
        for _ in range(len(que)):
            node=que.popleft()
            level.append(node.val)
            if node.left is not None:
                que.append(node.left)
            if node.right is not None:
                que.append(node.right)
        if len(parent)<1:
            parent.append(level[0])
        else:
            left.append(level[0])
            right.append(level[-1])
    print(parent,left,right)






n=TreeNode.TreeNode(1)
n.left=TreeNode.TreeNode(2)
n.right=TreeNode.TreeNode(3)
n.left.left=TreeNode.TreeNode(4)
n.left.right=TreeNode.TreeNode(5)
n.right.left=TreeNode.TreeNode(6)
n.right.right=TreeNode.TreeNode(7)
n.left.left.left=TreeNode.TreeNode(8)
print(Topview(n))