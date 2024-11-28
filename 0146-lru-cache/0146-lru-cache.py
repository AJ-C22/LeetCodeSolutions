class LRUCache:
    class Node:
        def __init__(self, key: int, val: int):
            self.key = key
            self.val = val
            self.prev = None  
            self.next = None  
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  
        self.left = LRUCache.Node(0, 0)  
        self.right = LRUCache.Node(0, 0)  
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node: 'LRUCache.Node'):
        node.prev.next = node.next
        node.next.prev = node.prev

    def add(self, node: 'LRUCache.Node'):
        self.right.prev.next = node
        node.prev = self.right.prev
        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            node = self.cache[key]
            self.remove(node)
            self.add(node)
            return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.add(node)
        else:
            if len(self.cache) == self.capacity:
                del self.cache[self.left.next.key]
                self.remove(self.left.next)
            
            new_node = LRUCache.Node(key, value)
            self.cache[key] = new_node
            self.add(new_node)


# Example usage:
# obj = LRUCache(2)
# print(obj.get(1))  # Example call
# obj.put(1, 1
