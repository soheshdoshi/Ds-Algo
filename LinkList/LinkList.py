class Node:
    def __init__(self,value):
        self.key=value
        self.next=None
class LinkList:
    def __init__(self):
        self.head=None
    def checkHead(self):
        if self.head is None:
            return 1
        return 0
    def insretEnd(self,value):
        new_node=Node(value)
        if self.checkHead():
            self.head=new_node
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=new_node
    def insertFront(self,value):
        new_node=Node(value)
        if self.checkHead():
            self.head=new_node
        else:
            new_node.next=self.head
            self.head=new_node
    def insertNodeatPostin(self,value,postion):
        if postion<1:
            self.insertFront(value)
        else:
            temp = self.head
            new_node = Node(value)
            while postion-1>0:
                if temp.next is None:
                    print("This postion not possible")
                    return
                else:
                    postion-=1
                    temp=temp.next
            new_node.next=temp.next
            temp.next=new_node
    def deletenodeatkey(self,key):
        if self.checkHead():
            print("Delete Op is not POssible")
            return
        temp=self.head
        if temp.key == key:
            self.head=temp.next
            temp=None
            return
        while temp:
            if temp.key==key:
                break
            prev=temp
            temp=temp.next
        if temp==None:
            print("key is not in list")
            return
        prev.next=temp.next
        temp=None
    def deleteFront(self):
        if self.checkHead():
            print("delete op is not possible.")
            return
        else:
            temp=self.head
            self.head=self.head.next
            #temp=None
            del temp
    def deleteEnd(self):
        if self.checkHead():
            print("delete op is not possible.")
        else:
            temp=self.head
            if temp.next is None:
                self.head=None
            while temp.next and temp.next.next:
                temp=temp.next
            temp.next=None
    def lenth(self):
        count=0
        if self.checkHead():
            return count
        temp=self.head
        while temp:
            count+=1
            temp=temp.next
        return count
    def serachELemnt(self,elment):
        if self.checkHead():
            print("No node is there")
            return
        else:
            temp=self.head
            while temp and temp.key!=elment:
                temp=temp.next
            if temp is None:
                print("No elemntfound.")
                return
            else:
                print("elemnt found")
                return
    def getNthNode(self,nth):
        if self.checkHead():
            print("No node in LinkliSt.")
            return
        lenth=self.lenth()
        if lenth<nth:
            print("linklist lenth is less")
            return
        else:
            temp=self.head
            while nth-1>0:
                temp=temp.next
                nth=nth-1
            return temp.key
    def nthnodeEnd(self,nth):
        if self.checkHead():
            print("No node in LL")
            return
        else:
            if self.lenth()<nth:
                print("Not possible.")
                return
            a=self.head
            b=self.head
            while nth-1>0:
                b=b.next
                nth-=1
            while b.next:
                b=b.next
                a=a.next
            return a.key
    def middlenode(self):
        if self.checkHead():
            print("No need in ll.")
            return
        else:
            a=self.head
            b=self.head
            while b.next and b.next.next:
                a=a.next
                b=b.next.next
            return a.key
    def keyCount(self,value):
        if self.checkHead():
            print("No node.")
            return
        else:
            count=0
            temp=self.head
            while temp:
                if temp.key==value:
                    count+=1
                temp=temp.next
            return count
    def detetct_loop(self):
        if self.checkHead():
            return 0
        else:
            a=self.head
            b=self.head
            while b and b.next:
                a=a.next
                b=b.next.next
                if a==b:
                    return 1
        return 0
    def printNode(self):
        if self.checkHead():
            print("No Node.")
            return
        else:
            temp=self.head
            while temp:
                print(temp.key)
                temp=temp.next


l=LinkList()
l.insretEnd(1)
l.insretEnd(2)
l.insretEnd(3)
l.insretEnd(4)
l.insretEnd(5)
l.insretEnd(6)
l.insretEnd(2)




