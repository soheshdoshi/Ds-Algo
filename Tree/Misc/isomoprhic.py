def mySolution(n1,n2):
    if n1 is None and n2 is None:
        return 1
    if n1 is None or n2 is None:
        return 0
    if n1.val!=n2.val:
        return 0
    return ((mySolution(n1.left,n2.left) and mySolution(n1.right,n2.right) )or (mySolution(n1.left,n2.right) and mySolution(n1.right,n2.left)))
