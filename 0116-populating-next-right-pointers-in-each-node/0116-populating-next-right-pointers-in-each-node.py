"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        visited = [root]
        queue = [root]
        if root == None:
            return None
        level = 0

        while queue:
            
            l = len(queue)
            

            for i in range(l):
                s = queue.pop(0)
                if i < l- 1:
                     s.next = queue[0]
                print(s.val)
                if s.left:
                    visited.append(s.left)
                    queue.append(s.left)
                if s.right:
                    visited.append(s.right)
                    queue.append(s.right)

            level += 1
        return root