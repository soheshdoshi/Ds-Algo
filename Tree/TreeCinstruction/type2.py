from Tree import Inorder
from Tree import TreeNode

def mySolution(arr,root,i,n):
    if i<n:
        temp=TreeNode.TreeNode(arr[i])
        root=temp
        root.left=mySolution(arr,root.left,2*i+1,n)
        root.right = mySolution(arr, root.right, 2 * i + 2, n)
    return root




a=[1,2,3,4,5,6,6,6,6]
n=len(a)
print(Inorder.inoderRecusion(mySolution(a,None,0,n)))
