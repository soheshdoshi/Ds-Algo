class Node:
    def __init__(self,value):
        self.next=None
        self.val=value
class LinkList:
    def __init__(self):
        self.head=None
    def push(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
        else:
            temp=self.head
            new_node.next = temp
            self.head=new_node
    def printList(self):
        temp=self.head
        while temp.next:
            print(str(temp.val)+"->",end="")
            temp=temp.next
        print(str(temp.val),end="")
    def revrseNode(self,node,mid):
        if node is None or node.next is None:
            return node
        else:
            prev=None
            curr=node
            while curr.val!=mid.val:
                next=curr.next
                curr.next=prev
                prev=curr
                curr=next
            prev=curr
            return prev
    def longestPalmdrom(self):
        if self.head is None:
            return 0
        if self.head.next is None:
            return 1
        else:
            max_lenth=1
            prev=self.head
            mid_p=prev.next
            prev.next=None
            node_check= mid_p.next
            while mid_p.next:
                rev=self.revrseNode(prev,mid_p)
                while rev.next and node_check:
                    count=0
                    if rev.key==node_check.key:
                        count+=1
                        rev=rev.next
                        node_check=node_check.next
                    




l=LinkList()
l.push(2)
l.push(2)
l.push(3)
l.push(1)
l.push(2)
l.push(2)
l.push(1)
l.push(2)
l.push(1)
l.push(2)
#l.printList()
l.longestPalmdrom()
l.printList()

