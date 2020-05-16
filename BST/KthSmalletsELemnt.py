
from Tree import TreeNode
def mySolution(node,k):
    print(kthSMallest(node,[]))

def kthSMallest(node,stack):
    if node:
        kthSMallest(node.left,stack)
        stack.append(node.val)
        kthSMallest(node.right,stack)
        return stack
    return stack
n=TreeNode.TreeNode(2)
n.left=TreeNode.TreeNode(1)
n.right=TreeNode.TreeNode(3)
print(mySolution(n,2))