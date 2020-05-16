def mySolution(node,stack,ans):
    if node:
        mySolution(node.left,ans,stack)
        ans[0]+=node.val
        stack.append(ans)
        mySolution(node.right,ans,stack)
        return stack
    else:
        return stack


def Solution(node):
    ans=[0]
    arr=mySolution(node,[],ans)
    return arr[0]