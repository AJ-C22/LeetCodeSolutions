"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if node == None:
            return None
        elif node.neighbors == []:
            node2 = Node(val=node.val)
            node2.neighbors = []
            return node2

        def dfs(node):
            d = {}
            stack = []
            visited = []
            if node:
                stack.append(node)
                visited.append(node)
            while stack:
                s = stack.pop()
                print(s.val)
                for neighbor in s.neighbors:
                    if neighbor not in visited:
                        stack.append(neighbor)
                        visited.append(neighbor)
                    if s.val in d:
                        d[s.val].append(neighbor.val)
                    else:
                        d[s.val] = [neighbor.val]

            return d

        d = dfs(node)
        print(d)
        if not node:
            return None

        new_node = Node(val=node.val)
        visited2 = {node.val: new_node}
        stack2 = [node]

        while stack2:
            s = stack2.pop()
            current_clone = visited2[s.val]

            ns = []
            for n in d[s.val]:
                if n not in visited2:
                    visited2[n] = Node(val=n)
                    stack2.append(visited2[n])
                ns.append(visited2[n])

            current_clone.neighbors = ns

        return new_node

                