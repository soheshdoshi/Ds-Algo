from collections import deque,defaultdict
from Tree import TreeNode
def mySolution(node):
    stack=[(node,0)]
    d = defaultdict(list)
    while stack:
        node,level=stack.pop()
        d[level].append(node.val)
        if node.left is not None:
            stack.append((node.left,level+1))
        if node.right is not None:
            stack.append((node.right,level-1))
    print(d)


def recusive(node,d,level):
    if node:
        d[level].append(node.val)
        recusive(node.left,d,level+1)
        recusive(node.right,d,level-1)
        return d


n=TreeNode.TreeNode(20)
n.left=TreeNode.TreeNode(8)
n.right=TreeNode.TreeNode(22)
n.right.left=TreeNode.TreeNode(4)
n.left.left=TreeNode.TreeNode(5)
n.left.right=TreeNode.TreeNode(3)
n.left.right.left=TreeNode.TreeNode(11)
n.left.right.right=TreeNode.TreeNode(14)
n.right.right=TreeNode.TreeNode(25)
# mySolution(n)
print(recusive(n,defaultdict(list),0))



