# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        def helper(root, l):
            if root == None:
                return
            l.append(root)
            helper(root.left,l)
            helper(root.right,l)

        r = []
        helper(root,r)
        for i in range(len(r)-1):
            r[i].left = None
            r[i].right = r[i+1]
        