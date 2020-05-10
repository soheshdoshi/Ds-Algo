from collections import deque
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

def nextPointer(node):
    curr=node
    que=deque()
    que.append(node)
    que.append(None)
    while que:
        node=que.popleft()
        if node!=None:
            node.next=que[0]
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)
        else:
            if len(que)>0:
                que.append(None)
    return curr


def levelpeinr(node):
    que=deque()
    que.append(node)
    while que:
        #print("newlebel")
        for _ in range(len(que)):
            node=que.popleft()
            temp=node.next
            print(temp)
            if node.left is not None:
                que.append(node.left)
            if node.right is not None:
                que.append(node.right)



n=TreeLinkNode(1)
n.left=TreeLinkNode(2)
n.right=TreeLinkNode(5)
n.left.left=TreeLinkNode(3)
n.left.right=TreeLinkNode(4)
n.right.left=TreeLinkNode(6)
n.right.right=TreeLinkNode(7)

levelpeinr(nextPointer(n))