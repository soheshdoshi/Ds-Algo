class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def printLeafNode(node):
    if node:
        printLeafNode(node.left)
        if node.left is None and node.right is None:
            print(node.data)
        printLeafNode(node.right)
def printLeftSide(node):
    if node:
        if node.left:
            print(node.data)
            printLeftSide(node.left)
        elif node.right:
            print(node.data)
            printLeftSide(node.right)


root = Node(20)
root.left = Node(8)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)
root.right = Node(22)
root.right.right = Node(25)
#printLeafNode(root)
printLeftSide(root)