# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []
        visited = set()
        start = 0
        queue = [[root, start]]

        def helper(root, count):
            if not root:
                return count
            return max(helper(root.right, count + 1), helper(root.left, count + 1)) 

        height = helper(root, 0)
        result = []

        for i in range(height):
            result.append([])

        while queue:
            node, height = queue.pop(0)
            if node.right:
                queue.append([node.right, height + 1])
            if node.left:
                queue.append([node.left, height + 1])
            result[height].append(node.val)
        
        answer = []
        for lst in result:
            answer.append(lst[0])
        return answer



        