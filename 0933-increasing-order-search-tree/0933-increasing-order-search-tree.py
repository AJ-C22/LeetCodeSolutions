# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        
        def recurse(node, l):
            if node == None:
                return 
            
            recurse(node.left, l)
            
            l.append(node.val)
            recurse(node.right, l)
        
        result = []
        recurse(root, result)
        print(result)
        r = TreeNode(result[0])
        curr = r
        for i in range(1, len(result)):
            curr.right = TreeNode(result[i])
            curr = curr.right
        
        return r

        