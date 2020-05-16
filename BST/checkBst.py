import Visulaztion
from Tree import TreeNode


def valid(node, lower, upper):
    if not node:
        return True
    if lower is not None and node.val <= lower:
        return False
    if upper is not None and node.val >= upper:
        return False
    return valid(node.left, lower, node.val) and valid(node.right, node.val, upper)



n=TreeNode.TreeNode(4)
n.left=TreeNode.TreeNode(2)
n.right=TreeNode.TreeNode(5)
n.left.left=TreeNode.TreeNode(1)
n.left.right=TreeNode.TreeNode(5)
print(checkBST(n))