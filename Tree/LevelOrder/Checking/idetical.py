def recursive(t1,t2):
    if t1 is None and t2 is None:
        return 1
    if t1 is not None and t2 is not None:
        return (t1.val==t2.vall) and recursive(t1.left,t2.left) and recursive(t1.right,t2.right)
    return False


def withoutRecusion(t1,t2):
    if t1 is None and t2 is None:
        return True
    if t1 is None or t2 is None:
        return False
    q1=[t1]
    q2=[t2]
    while q1 and q2:
        n1=q1.pop(0)
        n2=q2.pop(0)
        if n1.val!=n2.val:
            return False
        if n1.left and n2.left:
            q1.append(n1.left)
            q2.append(n2.left)
        elif n1.left or n2.left:
            return False
        if n1.right and n2.right:
            q1.append(n1.rigth)
            q2.append(n2.right)
        elif n1.right or n2.right:
            return False
    return True