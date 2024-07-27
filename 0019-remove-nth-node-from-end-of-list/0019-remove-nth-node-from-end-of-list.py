class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        fast = head
        slow = head

        for _ in range(n):
            if fast is None:  
                return head
            fast = fast.next

       
        if fast is None:
            return head.next 

        
        while fast.next is not None:
            fast = fast.next
            slow = slow.next #at total -n

       
        slow.next = slow.next.next

        return head
