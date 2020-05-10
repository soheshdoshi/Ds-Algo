from Tree import TreeNode


def SumOfTree(node,ans):
    if node is None:
        return ans
    return node.val+SumOfTree(node.left,ans)+SumOfTree(node.right,ans)



n=TreeNode.TreeNode(15)
n.left=TreeNode.TreeNode(10)
n.right=TreeNode.TreeNode(20)
n.left.left=TreeNode.TreeNode(8)
n.left.right=TreeNode.TreeNode(12)
n.right.left=TreeNode.TreeNode(16)
n.right.right=TreeNode.TreeNode(25)
print(SumOfTree(n,0))