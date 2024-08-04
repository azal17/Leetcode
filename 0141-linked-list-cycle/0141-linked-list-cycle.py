# Time Complexity: O(N),Space Complexity : O(1)
# Tortoise and Hare Algorithm 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        
        while fast is not None and fast.next != None: # has to be in loop cant be null
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
        return False
            