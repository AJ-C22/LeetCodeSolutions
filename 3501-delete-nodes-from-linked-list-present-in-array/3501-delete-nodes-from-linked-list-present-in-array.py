# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        n = len(nums)
        num_set = set()
        for i in range(n):
            num_set.add(nums[i])

        print(num_set)

        curr = head
        temp = ListNode()
        temp.next = head
        prev = temp

        while curr:
            if curr.val in num_set:
                prev.next = curr.next
                curr = curr.next
            else:
                prev = curr
                curr = curr.next 
                prev.next = curr
            print(prev.val)

        return temp.next


        