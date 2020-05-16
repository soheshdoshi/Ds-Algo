from Tree import TreeNode,Inorder


def mySolution(arr):
    if not  arr:
        return None
    midd=len(arr)//2
    node=TreeNode.TreeNode(arr[midd])
    node.left=mySolution(arr[:midd])
    node.right=mySolution(arr[midd+1:])
    return node



arr=[1,2,3,4,5,6,7]
Inorder.inoderRecusion(mySolution(arr))