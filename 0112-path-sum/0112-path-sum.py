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
            if root is None:
                return False  
            
            s += root.val  

            if root.left is None and root.right is None:
                if s == targetSum:
                    print("yes")
                    return True
                return False
            
            return helper(root.left, s) or helper(root.right, s)

        
        return helper(root, 0)
        