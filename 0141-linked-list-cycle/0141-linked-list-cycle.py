# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp = head
        hash = {}

        while temp is not None:
            if temp in hash:
                return True
            hash[temp] = temp.val
            temp = temp.next
        return False
        