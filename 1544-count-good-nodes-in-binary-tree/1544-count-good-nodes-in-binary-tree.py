# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(root, prev_max, final):
            if not root:
                return 

            if root.val >= prev_max:
                final.append(root.val)

            helper(root.left, max(prev_max, root.val), final)
            helper(root.right, max(prev_max, root.val), final)

        final = []
        helper(root, float('-inf'), final)
        return len(final)

            
            
        