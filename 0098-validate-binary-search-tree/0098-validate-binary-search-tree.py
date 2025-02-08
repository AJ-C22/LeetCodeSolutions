# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def helper(root, lower, upper):
            if root == None:
                return True
            if lower < root.val < upper:
                return helper(root.left, lower, root.val) and helper(root.right, root.val, upper)
            else:
                return False
            
        
        return helper(root, -1000000000000000, 1000000000000000)
        