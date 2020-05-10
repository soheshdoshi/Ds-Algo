from Tree import TreeNode
def lpr(node,ans):
    if node:
        lpr(node.left,ans)
        ans.append(node.val)
        lpr(node.right,ans)
        return ans
    else:
        return ans
def rpl(node,ans):
    if node:
        rpl(node.right,ans)
        ans.append(node.val)
        rpl(node.left,ans)
        return ans
    else:
        return ans

def without(n1,n2):
    if n1 is None and n2 is None:
        return 1
    if n1 is None or n2 is None:
        return 0
    if n1.left is not None and n2.right is not None:
        without(n1.left,n2.right)
        if n1.val!=n2.val:
            return 0
    if n1.right is not None and n2.left is not None:
        without(n1.right,n2.left)
    return 1
def mySolution(node1):
    # ans1=[]
    # ans2=[]
    # print(lpr(node1,ans1))
    # print(rpl(node1,ans2))
    cu1=node1
    cu2=node1
    return without(cu1,cu2)

n=TreeNode.TreeNode(1)
n.left=TreeNode.TreeNode(2)
n.right=TreeNode.TreeNode(2)
n.left.left=TreeNode.TreeNode(3)
n.left.right=TreeNode.TreeNode(4)
n.right.left=TreeNode.TreeNode(4)
n.right.right=TreeNode.TreeNode(3)
mySolution(n)