#User function Template for python3


'''

class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
'''

class Solution:
    def merge(self, list1, list2):
        dummyNode = Node(-1)
        temp = dummyNode
        
        while list1 and list2:
            if list1.data < list2.data:
                temp.bottom = list1
                temp = list1
                list1 = list1.bottom
            else:
                temp.bottom = list2
                temp = list2
                list2 = list2.bottom
            temp.next = None
        
        if list1:
            temp.bottom = list1
        else:
            temp.bottom = list2
        
        if dummyNode.bottom:
            dummyNode.bottom.next = None
        return dummyNode.bottom
                
    def flatten(self, root):
        if root == None or root.next == None:
            return root
    
        root.next = self.flatten(root.next)
        root = self.merge(root, root.next)
        
        return root



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