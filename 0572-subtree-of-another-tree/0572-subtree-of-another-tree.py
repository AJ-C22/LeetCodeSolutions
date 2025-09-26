# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        if not root or not subRoot:
            return True
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        def isEqual(tree1, tree2):
            if not tree1 and not tree2:
                return True
            if tree1 and not tree2:
                return False
            if tree2 and not tree1:
                return False
            print(tree1.val, tree2.val)
            if tree2.val != tree1.val:
                return False
            return (isEqual(tree1.left, tree2.left) and isEqual(tree1.right, tree2.right))
        
        stack = [root]
        while stack:
            node = stack.pop()
            if node.val == subRoot.val:
                eq = isEqual(node, subRoot)
                if eq:
                    return True
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        return False

        
        