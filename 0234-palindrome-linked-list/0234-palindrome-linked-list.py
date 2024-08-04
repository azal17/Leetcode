# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next




class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        q= head
        l = []
        while q is not None:
            l.append(q.val)
            q= q.next

        def palindrome(l : list) -> bool:
            return l == l[::-1]
        return palindrome(l)
            