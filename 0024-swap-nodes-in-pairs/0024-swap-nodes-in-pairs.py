# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        current = head
        prev = dummy

        while current and current.next:
            first = current
            second = current.next

            prev.next = second
            first.next = second.next
            second.next = first

            prev = first
            current = first.next
        return dummy.next
        