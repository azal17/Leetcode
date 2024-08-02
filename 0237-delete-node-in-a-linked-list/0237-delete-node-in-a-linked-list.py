# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        temp = node
        temp.val = temp.next.val
        temp.next = temp.next.next
        


        
        