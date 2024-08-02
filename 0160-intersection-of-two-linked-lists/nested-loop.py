#Time Complexity: O(m * n), Space Complexity: O(1) , optimal in space, not in time
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
     
        while headB != None:
            temp = headA
            while temp != None:
                if temp == headB:
                    return headB
                temp = temp.next
            headB = headB.next
        return None
