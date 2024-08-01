# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
        def reverseList(self,head):
            if head is None or head.next is None:
                return head

            new_head = self.reverseList(head.next)
            head.next.next = head
            head.next = None

            return new_head

        def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            dummy = ListNode(0)
            temp = dummy
            p = self.reverseList(l1)
            q = self.reverseList(l2)
            carry = 0
            
            while p is not None or q is not None or carry:
                sum_val = 0
                if p is not None:
                    sum_val += p.val
                    p = p.next
                if q is not None:
                    sum_val += q.val
                    q = q.next

                sum_val += carry 
                carry = sum_val // 10
                temp.next = ListNode(sum_val % 10)
                temp = temp.next
            
            k = dummy.next
            
        
            return k
