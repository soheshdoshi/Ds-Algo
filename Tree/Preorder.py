def withoutRecusion(node):
    stack=[node]
    while stack:
        temp=stack.pop()
        print(temp.val)
        if temp.right is not None:
            stack.append(temp.right)
        if temp.left is not None:
            stack.append(temp.left)