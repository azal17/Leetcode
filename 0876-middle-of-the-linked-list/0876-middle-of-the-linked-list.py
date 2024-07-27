#Tortoise and Hare algorithm.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def middleNode(self, head):
        slow = head
        fast = head

        while fast and fast.next and slow:
            fast = fast.next.next
            slow = slow.next
        return slow