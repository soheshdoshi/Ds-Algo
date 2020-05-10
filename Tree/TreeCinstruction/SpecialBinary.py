from Tree import TreeNode,Inorder


def genateTree(arr,strat,end):
    if strat>end or len(arr)==0:
        return
    index=arr.index(max(arr))
    Node=TreeNode.TreeNode(arr[index])
    Node.left=genateTree(arr[strat:index],strat,index-1)
    Node.right=genateTree(arr[index+1:end+1],index+1,end)
    return Node

def mySolution(arr):
    print(Inorder.inoderRecusion(genateTree(arr,0,len(arr)-1)))



mySolution([5,10,40,30,28])

