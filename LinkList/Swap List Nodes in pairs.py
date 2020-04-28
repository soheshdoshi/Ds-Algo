from .LinkList import LinkListNode

def mySolution(A):
    if A is None or A.next is None:
        return A
    prev=A
    curr=A.next
    A=curr
    while True:
        next_node=curr.next
        curr.next=prev
        if next_node is None or next_node.next is None:
            prev.next=next_node
            break
        prev.next=next_node.next
        prev=next_node
        curr=prev.next
    return A



# l=LinkListNode()
# l.pushNode(1)
# l.pushNode(2)
# l.pushNode(3)
# l.pushNode(4)
# l.printNode(l)