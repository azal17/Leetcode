# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def convert(self, a):
        n = len(a)
        dummy_node = ListNode(-1)
        temp = dummy_node

        for i in range(n):
            temp.next = ListNode(a[i])
            temp = temp.next 
        
        return dummy_node.next #  head 

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp_array = []
        p = list1
        q = list2

        while p is not None:
            temp_array.append(p.val)
            p = p.next
        
        while q is not None:
            temp_array.append(q.val)
            q = q.next
        
        temp_array.sort()

        head = self.convert(temp_array)
        return head
