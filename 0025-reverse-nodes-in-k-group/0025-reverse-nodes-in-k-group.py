# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,head):
        temp = head
        prev = None
        while temp is not None:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        return prev

    def getKnode(self, temp, k):
        k = k-1 # accomodates index 0
        while temp is not None and k>0:
            k = k-1
            temp = temp.next
        return temp

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        prevLast = None

        while temp is not None:
            knode = self.getKnode(temp, k)

            if knode is None:
                if prevLast:
                    prevLast.next = temp
                break

            nextNode = knode.next
            knode.next = None

            self.reverse(temp)

            if temp == head:
                head = knode
            else:
                prevLast.next = knode
            
            prevLast = temp
            temp = nextNode
        return head



            