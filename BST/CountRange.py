def countRange(node,B,C,count):
    if node:
        countRange(node.left,B,C,count)
        temp=node.val
        if temp>=B and temp<=C:
            count[0]+=1
        countRange(node.right,B,C,count)
        return count
    else:
        return count


def mySoution(node,B,C):
    count=[0]
    countRange(node,B,C,count)
    return count[0]