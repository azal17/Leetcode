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
        stack =[]

        while q is not None:
            stack.append(q.val)
            q = q.next
        q = head
        while q is not None:
            q.val = stack.pop()
            q = q.next

        return head

            
        
        
