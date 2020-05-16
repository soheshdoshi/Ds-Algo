def mySolution(node):
    if node is None or (node.left is None and node.right is None):
        return node
    else:
        node.left.val,node.right.val=node.right.val,node.left.val
        mySolution(node.left)
        mySolution(node.right)
        return node