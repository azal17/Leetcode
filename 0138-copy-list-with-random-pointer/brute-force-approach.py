# T.C = O(2n), S.C = O(N) + O(N)
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        temp = head
        mpp = {}
      
        while temp is not None:
            dummyNode = Node(temp.val)
            mpp[temp] = dummyNode
            temp = temp.next
        
        temp = head
        while temp is not None:
            copyNode = mpp[temp]
            copyNode.next = mpp.get(temp.next)
            copyNode.random = mpp.get(temp.random)
            temp = temp.next
        
        return mpp[head]
