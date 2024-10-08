#Time Complexity: O(m + n), Space Complexity: O(m), optimal for time not for space
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
     
        s,p ,q= set(),headA ,headB
        while p:
            s.add(p)
            p = p.next
        while q:
            if q in s:
                return q
            q = q.next
        return None
