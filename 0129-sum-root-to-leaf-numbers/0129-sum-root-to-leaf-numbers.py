# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        lst = []
        
        stack = [[root, lst]]
        result = []
        while stack:
            node, lst = stack.pop()
            curr_path = lst + [node.val]
            if node.right:
                stack.append([node.right, curr_path])
            if node.left:
                stack.append([node.left, curr_path])
            if not node.right and not node.left:
                result.append(curr_path)
        final = []
        for lst in result:
            l = len(lst)
            num = 0
            for i in range(l):
                num += lst[i] * 10**(l - 1 - i)
            final.append(num)
        
        return sum(final)
                

