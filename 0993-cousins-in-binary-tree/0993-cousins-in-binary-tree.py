# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: Optional[TreeNode]
        :type x: int
        :type y: int
        :rtype: bool
        """
        x_parent = [0]
        x_level = [0]
        y_level = [0]
        y_parent = [0]
        def helper(root,prev,level):
            if not root:
                return 
            if root.val == x:
                x_parent[0] = prev.val
                x_level[0] = level
            if root.val == y:
                y_parent[0] = prev.val
                y_level[0] = level
            helper(root.right, root, level + 1)
            helper(root.left, root, level + 1)
        
        start = TreeNode()
        print(x_parent, x_level, y_parent, y_level)
        helper(root, start, 0)
        if x_level == y_level and x_parent != y_parent:
            return True
        return False
            
            


        