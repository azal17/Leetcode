class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        
        dummy = ListNode(0)
        dummy.next = head
        q = dummy
        count = 0

        while q.next is not None:
            count +=1
            q = q.next
        
        actual_node_position = count - n
        q = dummy

        for _ in range(actual_node_position):
            q = q.next
        
        q.next = q.next.next

        return dummy.next


