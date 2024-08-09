#Time Limit Exceeded
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head

        for _ in range(k):
            temp = head
            while temp.next.next is not None:
                temp = temp.next
            end = temp.next
            temp.next = None
            end.next = head
            head = end
        return head
