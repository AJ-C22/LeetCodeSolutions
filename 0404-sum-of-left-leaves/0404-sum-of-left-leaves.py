# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def helper(root, prev):
            if not root:
                return 0
            print(root.val)
            if not root.right and not root.left and prev == "L":
                return root.val
            
            return helper(root.right, "R") + helper(root.left, "L")
        
        return helper(root, None)

        