from Tree import TreeNode


def isSumProperty(root):
    left_data, right_data = 0, 0

    if root == None or (root.left == None and root.right == None):
        return True
    else:
        if root.left:
            left_data = root.left.val

        if root.right:
            right_data = root.right.val

        if (root.val == left_data + right_data) and isSumProperty(root.left) and isSumProperty(root.right):
            return True
        return False



n=TreeNode.TreeNode(10)
n.left=TreeNode.TreeNode(8)
n.right=TreeNode.TreeNode(23)
n.left.left=TreeNode.TreeNode(3)
n.left.right=TreeNode.TreeNode(5)
n.right.left=TreeNode.TreeNode(2)

print(isSumProperty(n))
