# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        count = 0
        lst = []
        stack = [[root, count, lst]]
        result = []
        if not root:
            return []
        while stack:
            node, count, lst = stack.pop()
            curr_sum  = count + node.val
            curr_path = lst + [node.val]
            print(node.val)
            if node.right:
                stack.append([node.right, curr_sum, curr_path])
            if node.left:
                stack.append([node.left, curr_sum, curr_path])
            if not node.left and not node.right:
                if curr_sum == targetSum:
                    result.append(curr_path)
        return result
        
        