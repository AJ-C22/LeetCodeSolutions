# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def helper(root, height):
            if not root:
                return height
                
            right = helper(root.right, height + 1)
            left = helper(root.left, height + 1)
            return max(left, right)
            
            
        if not root:
            return True

        
        right = helper(root.right, 0)
        left = helper(root.left, 0)
        diff = abs(right - left)
        print(root.val)
        print(diff)
        if diff > 1:
            return False
        else:
            return self.isBalanced(root.right) and self.isBalanced(root.left)
        
