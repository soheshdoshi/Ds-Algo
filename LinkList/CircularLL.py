class Node:
    def __init__(self,value):
        self.next=None
        self.val=value
class CircularLinkList:
    def __init__(self):
        self.head=None
    def insertNode(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            new_node.next=self.head
        else:
            temp=self.head
            while temp.next!=self.head:
                temp=temp.next
            temp.next=new_node
            new_node.next=self.head
    def insertNoedatFornt(self,vale):
        new_node=Node(vale)
        if self.head is None:
            self.head=new_node
            new_node.next=self.head
        else:
            temp=self.head
            new_node.next=temp
            while temp.next!=self.head:
                temp=temp.next
            temp.next=None
            self.head=new_node
            temp.next=self.head
    def printNode(self):
        if self.head is None:
            return
        else:
            temp=self.head
            while temp.next!=self.head:
                print(temp.val)
                temp=temp.next
            print(temp.val)

l=CircularLinkList()
l.insertNoedatFornt(1)
l.insertNoedatFornt(2)
l.insertNoedatFornt(3)
l.printNode()