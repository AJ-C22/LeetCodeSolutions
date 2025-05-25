# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        curr = head
        l = 0
        while curr:
            l += 1
            curr = curr.next

        if l == 1:
            return None

        ind = l - n
        count = 1
        print("ind " + str(ind))
        if ind == 0:
            head = head.next
        curr = head
        while curr:
            print(curr.val)
            if count == ind:
                curr.next = curr.next.next
            curr = curr.next
            count += 1

        return head
        