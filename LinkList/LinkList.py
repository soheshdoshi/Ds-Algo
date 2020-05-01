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
    def loop_count(self):
        if self.checkHead():
            return 0
        else:
            a=self.head
            b=self.head
            while b and b.next:
                a=a.next
                b=b.next.next
                if a==b:
                    count=1
                    a=a.next
                    while a!=b:
                        count+=1
                        a=a.next
                    return count
            return 0


    def removeDuplicated(self):
        temp=self.head
        while temp.next:
            if temp.key==temp.next.key:
                new=temp.next.next
                temp.next=None
                temp.next=new
            else:
                temp=temp.next
    def swapNode(self,x,y):
        prevX=None
        currX=self.head
        while currX and currX.key!=x:
            prevX=currX
            currX=currX.next
        prevY=None
        currY=self.head
        while currY and currY.key!=y:
            prevY=currY
            currY=currY.next
        if currY== None or currX==None:
            return
        if prevX!=None:
            prevX.next=currY
        else:
            self.head=currY
        if prevY!=None:
            prevY.next=currX
        else:
            self.head=currX
        temp=currX.next
        currX.next=currY.next
        currY.next=temp
    def moveLastNode(self):
        if self.head is None or self.head.next is None:
            return
        else:
            fornt_node=self.head
            front_next=fornt_node.next
            fornt_node.next=None
            head=front_next
            while front_next.next.next:
                front_next=front_next.next
            t=front_next.next
            front_next.next=fornt_node
            self.head=t
            self.head.next=head
            #front_next.next = fornt_node
            #self.head.next=head
    def intersectionofNode(self,n1,n2):
        if n1 is None or n2 is None:
            return None
        p1=n1
        p2=n2
        new_node=Node(None)
        head=new_node
        while p1 and p2:
            if p1.key==p2.key:
                new_node.next=Node(p1.key)
                new_node=new_node.next
                p1=p1.next
                p2=p2.next
            elif p1.key>p2.key:
                p2=p2.next
            else:
                p1=p1.next
        self.head=head.next

    def revesedNode(self):
        if self.checkHead():
            return
        else:
            prev=None
            curr=self.head
            while curr:
                next=curr.next
                curr.next=prev
                prev=curr
                curr=next
            self.head=prev
    def printNode(self):
        if self.checkHead():
            print("No Node.")
            return
        else:
            temp=self.head
            while temp:
                print(temp.key)
                temp=temp.next
    def mergeTwoList(self,n1,n2):
        if n1 is None and n2 is None:
            return
        if n1 is None:
            return n2
        if n2 is None:
            return n1
        new_node=Node(None)
        self.head=new_node
        while n1 and n2:
            if n1.key<n2.key:
                new_node.next=Node(n1.key)
                n1=n1.next
            else:
                new_node.next=Node(n2.key)
                n2=n2.next
            new_node = new_node.next
        if n1 is not None:
            while n1:
                new_node.next=Node(n1.key)
                n1=n1.next
                new_node=new_node.next
        if n2 is not None:
            while n2:
                new_node.next = Node(n2.key)
                n2 = n2.next
                new_node = new_node.next
        self.head=self.head.next
    def deleteAlternate(self):
        temp=self.head
        while temp and temp.next:
            temp.next=temp.next.next
            temp=temp.next
    def rearrange(self):
        temp=self.head
        a=temp
        b=temp
        while b.next and b.next.next:
            a=a.next
            b=b.next.next
        b=a.next
        a.next=None
        prev=None
        curr=b
        while curr:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        b=prev
        new_node=Node(None)
        self.head=new_node
        while a and b:
            new_node.next=Node(a.key)
            new_node=new_node.next
            new_node.next=Node(b.key)
            new_node=new_node.next
            a=a.next
            b=b.next
        if a is not None:
            while a:
                new_node.next=Node(a.key)
                new_node=new_node.next
                a=a.next
        if b is not None:
            while b:
                new_node.next=Node(b.key)
                new_node=new_node.next
                b=b.next
        self.head=self.head.next
    def decimal_eq(self):
        self.revesedNode()
        temp=self.head
        ans=0
        i=0
        while temp:
            ans+=(temp.key*pow(2,i))
            i+=1
            temp=temp.next
        return ans
    def partionlist(self,x):
        temp=self.head
        smal=Node(None)
        large=Node(None)
        self.head=smal
        largehea=large
        while temp:
            if temp.key<x:
                smal.next=Node(temp.key)
                smal=smal.next
            else:
                large.next=Node(temp.key)
                large=large.next
            temp = temp.next
        smal.next=largehea.next
        self.head=self.head.next



# n=Node(1)
# n.next=Node(2)
# n.next.next=Node(3)
# n.next.next.next=Node(6)
#
# n1=Node(5)
# n1.next=Node(6)
# n1.next.next=Node(7)
# n1.next.next.next=Node(8)
#
# l=LinkList()
# l.mergeTwoList(n,n1)
# l.printNode()




l=LinkList()
l.insretEnd(1)
l.insretEnd(4)
l.insretEnd(3)
l.insretEnd(2)
l.insretEnd(5)
l.insretEnd(2)
l.insretEnd(3)
#l.printNode()
l.partionlist(3)
l.printNode()

