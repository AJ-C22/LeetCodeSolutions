# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        d = {}
        s = []
        curr = head
        while curr:
            s.append(curr)
            curr = curr.next

        i, j = 0, len(s) - 1
        while i < j:
            s[i].next = s[j]
            i += 1
            s[j].next = s[i]
            j -= 1
        
        s[i].next = None
            




        