# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if root == None:
            return False

        def helper(root, s):
            if root == None:
                return False
            if root.left == None and root.right == None:
                s += root.val
                if s == targetSum:
                    return True
                return False
            
            return helper(root.left, s + root.val) or helper(root.right, s + root.val)
        
        return helper(root, 0)
        