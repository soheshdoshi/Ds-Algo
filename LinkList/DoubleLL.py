class Node:
    def __init__(self,value):
        self.key=value
        self.next=self.prev=None
class DoubleLinkList:
    def __init__(self):
        self.head=None
    def insertAtFornt(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
        else:
            temp=self.head
            new_node.next=temp
            temp.prev=new_node
            self.head=new_node
    def insertAtEnd(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=new_node
            new_node.prev=temp
    def revse(self):
        if self.head is None or self.head.next is None:
            return
            #return self.head
        else:
            temp=None
            curr=self.head
            while curr:
                temp=curr.prev
                curr.prev=curr.next
                curr.next=temp
                curr=curr.prev
            self.head=temp.prev
    def kthNodeSwap(self,k):
        slw=self.head
        fast=self.head
        while k!=0:
            fast=fast.next
            k=k-1

    def printNode(self):
        if self.head is None:
            return
        else:
            temp=self.head
            while temp:
                print(temp.key)
                temp=temp.next


d=DoubleLinkList()
d.insertAtEnd(1)
d.insertAtEnd(2)
d.revse()
d.printNode()

