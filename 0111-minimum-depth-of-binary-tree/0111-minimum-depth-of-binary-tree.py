# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        count = 0
        stack = [[root, count]]
        result = []
        while stack:
            node, num = stack.pop()
            print(num)
            if node.right:
                stack.append([node.right, num + 1])
            if node.left:
                stack.append([node.left, num + 1])
            if not node.right and not node.left:
                result.append(num)
        
        return min(result) + 1
        