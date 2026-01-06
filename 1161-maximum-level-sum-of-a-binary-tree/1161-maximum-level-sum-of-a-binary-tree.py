# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def find_max(root, count):
            if not root:
                return count
            return max(find_max(root.left, count + 1), find_max(root.right, count + 1))

        m = find_max(root, 0)

        d = {i : 0 for i in range(1,m + 1)}
        def helper(root, level):
            if not root:
                return
            d[level] += root.val
            helper(root.left, level + 1)
            helper(root.right, level + 1)
            
        helper(root,1)
        print(d)
        curr_max = [0,float("-inf")]
        for key, value in d.items():
            if value > curr_max[1]:
                curr_max = [key,value]

        return curr_max[0]
        
        
        

        