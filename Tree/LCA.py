def lcaRecusrive(node,n1,n2,arr):
    if node is None:
        return node
    if node.val==n1:
        arr[0]=True
        return node
    if node.val==n2:
        arr[1]=True
        return node
    lefe_side=lcaRecusrive(node.left,n1,n2,arr)
    right_side=lcaRecusrive(node.right,n1,n2,arr)
    if lefe_side and right_side:
        return node
    if lefe_side is not None:
        return lefe_side
    else:
        return right_side
def findKey(node,key):
    if node is None:
        return node
    if node.val==key or findKey(node.left,key) or findKey(node.right,key):
        return True
    return False

def mySolution(node,n1,n2):
    arr=[False,False]
    lca=lcaRecusrive(node,n1,n2,arr)
    if arr[0] and arr[1] or arr[0] and findKey(lca,n2) or arr[1] and findKey(lca,n1):
        return lca
    return None


