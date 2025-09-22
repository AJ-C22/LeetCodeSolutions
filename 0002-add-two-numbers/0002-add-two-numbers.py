# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr1 = l1
        curr2 = l2
        lst1 = []
        lst2 = []
        while curr1:
            lst1.append(curr1.val)
            curr1 = curr1.next
        while curr2:
            lst2.append(curr2.val)
            curr2 = curr2.next

        num1 = 0
        num2 = 0
        mult = 1
        for i in range(len(lst1)):
            num1 += lst1[i] * mult
            mult *= 10
        mult = 1
        for i in range(len(lst2)):
            num2 += lst2[i] * mult
            mult *= 10
        print(num1)
        print(num2)
        final = num1 + num2

        mod = 10
        result = []

        print(final)
        if final == 0:
            result = [0]
        else:
            result = []
            while final > 0:
                result.append(final % 10)
                final //= 10
        
        new = ListNode()
        curr = new

        dummy = ListNode(0)
        cur = dummy
        for val in result:
            cur.next = ListNode(val)
            cur = cur.next

        return dummy.next