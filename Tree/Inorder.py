from Tree import TreeNode

def inoderRecusion(node):
    if node:
        inoderRecusion(node.left)
        print(node.val)
        inoderRecusion(node.right)

def withoutRecusion(node):
    stack=[]
    while True:
        if node is not None:
            stack.append(node)
            node=node.left
        elif stack:
            node=stack.pop()
            print(node.val)
            node=node.right
        else:
            break










n=TreeNode.TreeNode(1)
n.left=TreeNode.TreeNode(2)
n.right=TreeNode.TreeNode(3)
n.left.left=TreeNode.TreeNode(4)
n.left.right=TreeNode.TreeNode(5)
#inoderRecusion(n)
withoutRecusion(n)