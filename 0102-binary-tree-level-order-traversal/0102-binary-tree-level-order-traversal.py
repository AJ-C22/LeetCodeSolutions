# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        level = 0
        lst = []
        def counter(root, count):
            if not root:
                return count
            return max(counter(root.left, count + 1), counter(root.right, count + 1))
        count = counter(root,0)
        print(count)
        for i in range(count):
            lst.append([])

        def helper(root, level, lst):
            if not root:
                return 
            lst[level].append(root.val)
            helper(root.left, level + 1, lst)
            helper(root.right, level + 1, lst)

        helper(root, level, lst)
        return lst
        