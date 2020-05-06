from collections import deque
from Tree import TreeNode
def LevelOderSpiral(node):
    que=deque()
    if node:
        que.append(node)
    ans=[]
    count = 0
    while que:
        level=[]
        for _ in range(len(que)):
            x=que.popleft()
            level.append(x)
            if x.left:
                que.append(x.left)
            if x.right:
                que.append(x.right)
        if count%2==0:
            ans.append(level)
        else:
            ans.append(reversed(level))
        count+=1
    return ans


