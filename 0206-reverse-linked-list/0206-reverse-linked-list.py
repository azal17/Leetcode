# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    class ListNode(object):
        def __init__(self, val =0, next = None):
            self.val = val
            self.next = next
    def reverseList(self, head):
        q = head

        prev = None

        while q is not None:
            front = q.next
            q.next = prev
            prev = q
            q = front
        return prev