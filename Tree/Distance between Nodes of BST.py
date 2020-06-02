def find_lca(node,a,b):
    if node is None:
        return node
    if node.val == a or node.val == b:
        return node
    left=find_lca(node.left,a,b)
    right=find_lca(node.right,a,b)
    if left is not None and right is not None:
        return node
    if left:
        return left
    else:
        return right

def findLevel(node,value,d,level):
    if node is None:
        return
    if node.val==value:
        d.append(level)
        return
    findLevel(node.left,value,d,level+1)
    findLevel(node.right,value,d,level+1)

def findDistnce(node,a,b):
    lca=find_lca(node,a,b)
    d1=[]
    d2=[]
    findLevel(lca,a,d1,0)
    findLevel(lca,b,d2,0)
    return d1[0]+d2[0]