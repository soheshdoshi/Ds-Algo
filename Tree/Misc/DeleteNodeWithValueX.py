def mySolution(node,x):
    if node is None:
        return node
    mySolution(node.left,x)
    mySolution(node.right,x)
    if node.val==x:
        node=None
