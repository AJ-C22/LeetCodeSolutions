# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        max_sum = [0]  # Using a list to store max_sum as a mutable variable

        def helper(node):
            if not node:
                return 0

            left_depth = helper(node.left)
            right_depth = helper(node.right)

            # Update max sum of left + right subtree depths at this node
            max_sum[0] = max(max_sum[0], left_depth + right_depth)

            # Return the depth of the current subtree
            return max(left_depth, right_depth) + 1

        helper(root)
        return max_sum[0]


        