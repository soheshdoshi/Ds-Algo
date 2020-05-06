from  Tree import TreeNode
def nthnodeofinoder(node,nth):
    stack=[]
    ans=[]
    count=0
    while True:
        if node is not None:
            stack.append(node)
            node=node.left
        elif stack:
            node=stack.pop()
            ans.append(node.val)
            count+=1
            if count==nth:
                print(node.val)
            node=node.right
        else:
            break
    return ans



n=TreeNode.TreeNode(1)
n.left=TreeNode.TreeNode(2)
n.right=TreeNode.TreeNode(3)
n.left.left=TreeNode.TreeNode(4)
n.left.right=TreeNode.TreeNode(5)
print(nthnodeofinoder(n,1))