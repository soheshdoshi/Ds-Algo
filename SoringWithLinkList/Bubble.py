class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        swap = 0
        if head != None:
            while (1):

                swap = 0
                tmp = head
                while (tmp.next != None):
                    if tmp.val > tmp.next.val:
                        # swap them
                        swap += 1
                        p = tmp.val
                        tmp.val = tmp.next.val
                        tmp.next.val = p
                        tmp = tmp.next
                    else:
                        tmp = tmp.next

                if swap == 0:
                    break
                else:
                    continue

            return head
        else:
            return head