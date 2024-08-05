#User function Template for python3



class Node:
    def __init__(self, data=None, next=None, bottom=None):
        self.data = data
        self.next = next
        self.bottom = bottom

class Solution:
    def flatten(self, root: Node) -> Node:
        if not root:
            return None
        
       
        nodes = []
        temp = root
        while temp:
            current = temp
            while current:
                nodes.append(current)
                current = current.bottom
            temp = temp.next
        
     
        nodes.sort(key=lambda x: x.data)
        
        if not nodes:
            return None
        
      
        head = nodes[0]
        temp = head
        
        for node in nodes[1:]:
            temp.bottom = node
            temp = temp.bottom
       
        if temp:
            temp.bottom = None
        
        return head

                
    
            
      


#{ 
 # Driver Code Starts
#Initial Template for Python 3


class Node:

    def __init__(self, d):
        self.data = d
        self.next = None
        self.bottom = None


def printList(node):
    while (node is not None):
        print(node.data, end=" ")
        node = node.bottom

    print()


if __name__ == "__main__":
    t = int(input())
    while (t > 0):
        head = None
        arr = []

        arr = [int(x) for x in input().strip().split()]
        N = len(arr)
        temp = None
        tempB = None
        pre = None
        preB = None

        flag = 1
        flag1 = 1
        listo = [int(x) for x in input().strip().split()]
        it = 0
        for i in range(N):
            m = arr[i]
            m -= 1
            a1 = listo[it]
            it += 1
            temp = Node(a1)
            if flag == 1:
                head = temp
                pre = temp
                flag = 0
                flag1 = 1
            else:
                pre.next = temp
                pre = temp
                flag1 = 1

            for j in range(m):
                a = listo[it]
                it += 1
                tempB = Node(a)
                if flag1 == 1:
                    temp.bottom = tempB
                    preB = tempB
                    flag1 = 0
                else:
                    preB.bottom = tempB
                    preB = tempB
        ob = Solution()
        root = ob.flatten(head)
        printList(root)

        t -= 1

# } Driver Code Ends