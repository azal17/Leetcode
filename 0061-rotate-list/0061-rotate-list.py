# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None or k == 0 :
            return head

        count = 1
        temp = head

        while temp.next is not None:
            count +=1
            temp = temp.next

        temp.next = head
        k = k % count
        new_tail = count - k

        while new_tail != 0:
            temp = temp.next
            new_tail -= 1
        
        head = temp.next
        temp.next = None

        return head
        