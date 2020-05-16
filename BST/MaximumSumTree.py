import sys
def valid(node, lower, upper):
    if not node:
        return True
    if lower is not None and node.val <= lower:
        return False
    if upper is not None and node.val >= upper:
        return False
    return valid(node.left, lower, node.val) and valid(node.right, node.val, upper)

def recusion(node,count,max_e,lower,upper):
    if not node:
        max_e[0]=count[0]
        return max_e
    if lower is not  None

def mySolution(node):
    count=[0]
    Max_elemnt=[-sys.maxsize-1]