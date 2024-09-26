class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.count = 1  
        self.prev = None
        self.next = None

class List:
    def __init__(self):
        self.head = Node(0, 0)  
        self.tail = Node(0, 0)  
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0 

    def add_front(self, node: Node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def remove(self, node: Node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        self.size -= 1

    def pop_back(self) -> Node:
        if self.size > 0:
            last_node = self.tail.prev
            self.remove(last_node)
            return last_node
        return None

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  
        self.freq_map = {}  
        self.min_freq = 0  
        self.curr_size = 0  

    def update_freq(self, node: Node):
        freq = node.count
        self.freq_map[freq].remove(node)
        if self.freq_map[freq].size == 0:
            del self.freq_map[freq]
            if self.min_freq == freq:
                self.min_freq += 1
        node.count += 1
        new_freq = node.count
        if new_freq not in self.freq_map:
            self.freq_map[new_freq] = List()
        self.freq_map[new_freq].add_front(node)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.update_freq(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.update_freq(node)
        else:
            if self.curr_size >= self.capacity:
                lfu_list = self.freq_map[self.min_freq]
                lfu_node = lfu_list.pop_back()
                del self.cache[lfu_node.key]
                self.curr_size -= 1


            new_node = Node(key, value)
            self.cache[key] = new_node
            if 1 not in self.freq_map:
                self.freq_map[1] = List()
            self.freq_map[1].add_front(new_node)
            self.min_freq = 1  
            self.curr_size += 1




# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)R