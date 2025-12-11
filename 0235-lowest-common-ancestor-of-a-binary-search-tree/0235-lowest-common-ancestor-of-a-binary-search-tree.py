# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                print(node.val)
                if node.val > p.val and node.val > q.val:
                    print("LEFT")
                    if node.left:
                        stack.append(node.left)
                elif node.val < p.val and node.val < q.val:
                    print(p,q)
                    print("RIGHT")
                    if node.right:
                        stack.append(node.right)
                else:
                    return node
                    
        