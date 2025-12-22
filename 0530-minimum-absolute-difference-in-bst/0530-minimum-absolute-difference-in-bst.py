# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        stack = [root]
        lst = []
        while stack:
            node = stack.pop()
            if not node:
                continue
            lst.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
        lst.sort()
        
        m = float("inf")
        for i in range(1,len(lst)):
            cur = abs(lst[i] - lst[i-1])
            if cur < m:
                m = cur
                
        return m
        
        