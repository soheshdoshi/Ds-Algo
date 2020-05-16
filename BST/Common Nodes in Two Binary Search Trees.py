def mySolution(node1,node2,count):
    s1=[]
    s2=[]
    while True:
        if node1:
            s1.append(node1)
            node1=node1.next
        elif node2:
            s2.append(node2)
            node2=node2.next
        elif len(s1)!=0 and len(s2)!=0:
            node1=s1[-1]
            node2=s2[-1]
            if node1.val==node2.val:
                count+=1
                s1.pop(-1)
                s2.pop(-1)
                node1=node1.right
                node2=node2.right
            elif node1.val<node2.val:
                s1.pop(-1)
                node1=node1.right
                node2=None
            elif node1.val>node2.val:
                s2.pop(-1)
                node2=node2.right
                node1=None
        else:
            break
    return count%((10**9)+7)

# def genrateHash(node1,arr_set):
#     if node1:
#         genrateHash(node1.left,arr_set)
#         arr_set.add(node1.val)
#         genrateHash(node1.right,arr_set)
#     else:
#         return arr_set
# def mySolution(node2,hash_set,count):
#     if node2:
#         mySolution(node2.left,hash_set,count)
#         if node2.val in hash_set:
#             count[0]+=1
#         mySolution(node2.right,hash_set,count)
#         return count
#     else:
#         return count
# def findCount(node1,node2):
#     hash_set=set()
#     hash_set=genrateHash(node1,hash_set)
#     count=[0]
#     mySolution(node2,hash_set,count)
#     return count[0]%((10**9)+7)



def mySolution(node1,nodd2):