class Node:
    def __init__(self, data=None, next=None, bottom=None):
        self.data = data
        self.next = next
        self.bottom = bottom

class Solution:
    def flatten(self, root: Node) -> Node:
        if not root:
            return None
        
       
        nodes = []
        temp = root
        while temp:
            current = temp
            while current:
                nodes.append(current)
                current = current.bottom
            temp = temp.next
        
     
        nodes.sort(key=lambda x: x.data)
        
        if not nodes:
            return None
        
      
        head = nodes[0]
        temp = head
        
        for node in nodes[1:]:
            temp.bottom = node
            temp = temp.bottom
       
        if temp:
            temp.bottom = None
        
        return head
