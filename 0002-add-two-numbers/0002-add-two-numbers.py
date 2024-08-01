class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        temp = dummy
        carry = 0
        
        while l1 is not None or l2 is not None or carry:
            sum_val = carry
            if l1 is not None:
                sum_val += l1.val
                l1 = l1.next
            if l2 is not None:
                sum_val += l2.val
                l2 = l2.next
            
            carry = sum_val // 10
            temp.next = ListNode(sum_val % 10)
            temp = temp.next
        
        return dummy.next