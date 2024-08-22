"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

       
        temp = head
        while temp is not None:
            dum = Node(temp.val)
            dum.next = temp.next
            temp.next = dum
            temp = dum.next
        temp = head

        while temp is not None:
            if temp.random is not None:
                temp.next.random = temp.random.next
            temp = temp.next.next

        temp = head
        dummyNode = Node(-1) 
        copy = dummyNode
        while temp is not None:
            copy.next = temp.next  
            temp.next = temp.next.next  
            copy = copy.next 
            temp = temp.next 
        return dummyNode.next  