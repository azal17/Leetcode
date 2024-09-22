class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  
        self.key_freq = {}  
        self.freq_list = {} 
        self.min_freq = 0 

    def addnode(self, node: Node, freq: int):
        if freq not in self.freq_list:
            self.freq_list[freq] = DoublyLinkedList()
        self.freq_list[freq].add_to_front(node)

    def delnode(self, node: Node, freq: int):
        self.freq_list[freq].remove(node)
        if self.freq_list[freq].is_empty():
            del self.freq_list[freq]
            if self.min_freq == freq:
                self.min_freq += 1

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        freq = self.key_freq[key]

        self.delnode(node, freq)

        self.key_freq[key] = freq + 1
        self.addnode(node, freq + 1)

        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.cache:

            node = self.cache[key]
            node.value = value
            freq = self.key_freq[key]
            self.delnode(node, freq)
            self.key_freq[key] = freq + 1
            self.addnode(node, freq + 1)
        else:
            if len(self.cache) >= self.capacity:
    
                lfu_node = self.freq_list[self.min_freq].pop_back()
                del self.cache[lfu_node.key]
                del self.key_freq[lfu_node.key]

            new_node = Node(key, value)
            self.cache[key] = new_node
            self.key_freq[key] = 1
            self.min_freq = 1
            self.addnode(new_node, 1)

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_to_front(self, node: Node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def remove(self, node: Node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def pop_back(self) -> Node:
        if self.is_empty():
            return None
        lru_node = self.tail.prev
        self.remove(lru_node)
        return lru_node

    def is_empty(self):
        return self.head.next == self.tail
