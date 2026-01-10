# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def helper(root, path, lst):
            if not root:
                return 
            path = path + [root.val]
            if not root.right and not root.left:
                lst.append(path)
            helper(root.right, path, lst)
            helper(root.left, path, lst)

        lsts = []
        path = []
        helper(root, path, lsts)
        result = []
        for num in lsts:
            l = len(num)
            s = 0
            for digit in num:
                s += digit * 10**(l-1)
                l -= 1
            result.append(s)

        return sum(result)



        print(lst)


        
        