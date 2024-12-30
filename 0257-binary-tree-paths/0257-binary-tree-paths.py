# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        
        def helper(l, root, s, status):
            if root == None:
                return
            if root.right == None and root.left == None:
                if not status:
                    s = s + "->"
                s += str(root.val)
                return l.append(s)
            
            if not status:
                s = s + "->"
            s += str(root.val)

            helper(l, root.right, s, False)
            helper(l, root.left, s, False)
        
        path = ''
        result = []
        helper(result, root, path, True)
        return result
        