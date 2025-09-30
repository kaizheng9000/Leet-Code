
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        # Dummy nodes for easy access to LRU and MRU nodes
        self.head = Node(0,0)
        self.tail = Node(0,0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node: Node):
        # Set links for new node
        prev = node.prev
        nxt = node.next

        # Set links for existing nodes to the new node
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node: Node):

        # I'm inserting at the head, which I consider to be the most recently used
        nxt = self.head.next
        prev = self.head

        # Set links for the new node
        node.prev = prev
        node.next = nxt

        # Set links for existing nodes to new node
        prev.next = node
        nxt.prev = node



    def get(self, key: int):
        # Make sure the node exists, then remove and insert so that it's the MRU
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int):
        # Need to take out the node if it's already there so we don't have duplicates
        #  in the cache
        if key in self.cache:
            # Could just update the node value instead of removing the node and creating another
            self.remove(self.cache[key])

        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        # Purge the LRU node if the capacity is exceeded
        if len(self.cache) > self.cap:
            lru = self.tail.prev
            self.remove(lru)
            del self.cache[lru.key]


["LRUCache", [2], "put", [1, 10],  "get", [1], "put", [2, 20], "put", [3, 30], "get", [2], "get", [1]]

cache = LRUCache(2)
print(cache.put(1, 10))
print(cache.get(1))
print(cache.put(2, 20))
print(cache.put(3, 30))
print(cache.get(2))
print(cache.get(1))