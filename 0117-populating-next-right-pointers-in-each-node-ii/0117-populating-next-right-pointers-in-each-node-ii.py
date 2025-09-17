"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """

        if not root:
            return root

        queue = deque([(root, 0)])

        while queue:
            node, height = queue.popleft()
            if queue and queue[0][1] == height:
                node.next = queue[0][0]
            else:
                node.next = None
            if node.left:
                queue.append([node.left, height + 1])
            if node.right:
                queue.append([node.right, height + 1])

        return root

        