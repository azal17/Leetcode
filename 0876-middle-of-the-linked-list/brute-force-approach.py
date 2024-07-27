# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def middleNode(self, head):
        if head is None or head.next is None:
            return head

        temp = head
        count = 0

        
        while temp is not None:
            count += 1
            temp = temp.next

      
        mid = count //2
        temp = head
        
        for _ in range(mid):
            temp = temp.next
        return temp
        
