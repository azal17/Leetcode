# without additional space, Tortoise and Hare Algorithm
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverse(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head  
        new_head = self.reverse(head.next)
        head.next.next = head
        head.next = None
        return new_head

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return True  
        
      
        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        
      
        s = slow.next
        head2 = self.reverse(s)

        first_half = head
        second_half = head2
        
        while second_half is not None:
            if first_half.val != second_half.val:
                return False
            first_half = first_half.next
            second_half = second_half.next
        
        return True
