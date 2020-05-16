class TreeNode:
    def __init__(self,value):
        self.left=self.right=None
        self.val=value

def findLCA(node,n1,n2):
    if node is None:
        return node
    if node.val ==n1 or node.val==n2:
        return node
    left=findLCA(node.left,n1,n2)
    right=findLCA(node.right,n1,n2)
    if left is not None and right is not None:
        return node
    if left:
        return left
    else:
        return right

def finddistnce(node,key,d,level):
    if node is None:
        return 0
    if node.val==key:
        return level
    finddistnce(node.left,key,d,level+1)
    finddistnce(node.right, key, d, level + 1)
    return level



n=TreeNode(1)
n.left=TreeNode(2)
n.right=TreeNode(3)
n.left.left=TreeNode(4)
n.left.right=TreeNode(5)
n.right.left=TreeNode(6)
n.right.right=TreeNode(7)
print(finddistnce(findLCA(n,5,6),5,[],0))