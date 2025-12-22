# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: bool
        """
        if root and not root.right and not root.left:
            return False
        stack = [root]
        d = set()
        while stack:
            node = stack.pop()
            if not node:
                continue
            if k - node.val in d:
                return True
            if node.val not in d:
                d.add(node.val)
            
            stack.append(node.right)
            stack.append(node.left)
        
        return False


        
        