from heapq import heappush,heappop,heapify,heapreplace


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # @param A : list of linked list
    # @return the head node in the linked list
    def mergeKLists(self, A):
        value,head,poinet=[],None,None
        for l in A:
            while l:
                heappush(value,l.val)
                l=l.next
        while value:
            if head==None:
                head=ListNode(heappop(value))
                poinet=head
            else:
                poinet.next=ListNode(heappop(value))
                poinet=poinet.next
        return head

