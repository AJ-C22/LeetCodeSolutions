# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        queue = [root]
        level = 0
        levels = []
        d = {}
        d[root.val] = None
        while queue:
            r = len(queue)
            levels.append([])
            for _ in range(r):
                node = queue.pop(0)
                levels[level].append(node.val)
                if not node:
                    continue
                if node.left:
                    d[node.left.val] = node.val
                    queue.append(node.left)
                if node.right:
                    d[node.right.val] = node.val
                    queue.append(node.right)

            level += 1

        print(levels)
        print(d)
        deepest = levels.pop()
        result = []

        if len(deepest) == 1:
            answer = deepest[0]
        else:
            while True:
                for node in deepest:
                    result.append(d[node])
                # 2, 2, 6
                if all(node == result[0] for node in result):
                    answer = result[0]
                    break
                deepest = result
                result = []

        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if node.val == answer:
                    return node
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        # 7: 2
        # 4: 2
        # 9: 6
            