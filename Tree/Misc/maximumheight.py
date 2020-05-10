from Tree import TreeNode
def maximumHeight(node):
    if node is None:
        return 0
    else:
        left=maximumHeight(node.left)
        right=maximumHeight(node.right)
        return max(left,right)+1
