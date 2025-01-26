# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        def helper(root, l):
            if root == None:
                return
            helper(root.left, l)
            l.append(root.val)
            helper(root.right, l)
        
        result = []
        helper(root,result)
        return result