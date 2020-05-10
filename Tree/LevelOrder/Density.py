class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def Height(node):
    if node is None:
        return 0
    return max(1+Height(node.left),1+Height(node.right))
def size(node,count):
    if node:
        count+=1
        size(node.left,count)
        size(node.right,count)
    return count


root = Node(20)
root.left = Node(8)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)
root.right = Node(22)
root.right.right = Node(25)
print(Height(root))
print(size(root,0))