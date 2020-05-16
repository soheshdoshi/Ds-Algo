from Tree import TreeNode,Inorder

def insertNode(node,value):
    new_node = TreeNode.TreeNode(value)
    if node is None:
        node=new_node
        return node
    else:
        if node.val>=value:
            if node.left is None:
                node.left=new_node
            else:
                insertNode(node.left,value)
        else:
            if node.right is None:
                node.right=new_node
            else:
                insertNode(node.right,value)
        return node
def searchNode(node,vale):
    if node.val == vale:
        return node.val
    if node.val>=vale:
        if node.left:
            searchNode(node.left,vale)
        else:
            return -1
    elif node.val<vale:
        if node.right:
            searchNode(node.right,vale)
        else:
            return -1
    else:
        return -1


def deleltenode(node,value):
    if node is None:
        print("No Node is there")
        return
    if node.val<value:
        node.left=deleltenode(node.left,value)
    elif node.val>value:
        node.right=deleltenode(node.right,val)
    

n=insertNode(None,5)
n=insertNode(n,2)
n=insertNode(n,3)
n=insertNode(n,6)
n=insertNode(n,1)
n=insertNode(n,7)
Inorder.inoderRecusion(n)
print(searchNode(n,10))



