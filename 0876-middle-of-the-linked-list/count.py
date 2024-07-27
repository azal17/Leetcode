# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def middleNode(self, head):
        count = 0
        q = head
        while q is not None:
            q = q.next
            count += 1
        
       
        mid = ceil(count / 2)
        
        q = head
        index = 0
        new_head = None
        new_tail = None
        
        while q is not None:
            if index >= mid:
                if new_head is None:
                    new_head = ListNode(q.val)
                    new_tail = new_head
                else:
                    new_tail.next = ListNode(q.val)
                    new_tail = new_tail.next
            q = q.next
            index += 1
        
        return new_head
