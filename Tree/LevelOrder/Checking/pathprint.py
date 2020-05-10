
class getNode:
    def __init__(self, data):
        self.val = data
        self.left = self.right = None
def genratePath(node,arr,key):
    if not node:
        return False
    arr.append(node.val)
    if node.val==key:
        return True
    if genratePath(node.left,arr,key) or genratePath(node.right,arr,key):
        return True
    arr.pop()
    return False
def mySolution(node,key):
    arr=[]
    if genratePath(node,arr,key):
        print(arr)
root = getNode(1)
root.left = getNode(2)
root.right = getNode(3)
root.left.left = getNode(4)
root.left.right = getNode(5)
root.right.left = getNode(6)
root.right.right = getNode(7)
mySolution(root,66)