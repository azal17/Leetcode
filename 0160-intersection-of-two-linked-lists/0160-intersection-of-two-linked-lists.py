class Solution:
     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headB or not headA:
            return None
        
        p,q = headA, headB

        while p != q:
            p = p.next if p else headB
            q = q.next if q else headA
        return q
