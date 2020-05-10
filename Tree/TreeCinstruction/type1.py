from Tree import TreeNode


def genrateTree(inorder, preorder, strat, end):
    if strat > end:
        return
    Node = TreeNode.TreeNode(preorder[genrateTree.preindex])
    genrateTree.preindex += 1
    if strat==end:
        return Node
    index=inorder.index(preorder[Node.val])
    Node.left=genrateTree(inorder,preorder,strat,index-1)
    Node.right=genrateTree(inorder,preorder,index+1,end)
    return Node


def mySolution(inorder, preorder):
    lenth = len(inorder)
    strat = 0
    end = lenth - 1
    return genrateTree(inorder,preorder,strat,end)

genrateTree.preindex = 0

