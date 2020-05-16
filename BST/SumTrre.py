from Tree import TreeNode,Inorder

def recusion(node,sum):
    if node:
        recusion(node.left,sum)
        sum[0]+=node.val
        node.val=sum[0]
        recusion(node.right,sum)
def mySolution(node):
    sum=[0]
    recusion(node,sum)


n=TreeNode.TreeNode(5)
n.left=TreeNode.TreeNode(2)
n.right=TreeNode.TreeNode(13)
mySolution(n)
Inorder.inoderRecusion(n)


