class Node:
    def __init__(self, val = 0):
        self.val = val
        self.next = None
class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size =  0

        
        

    def get(self, index: int) -> int:
        q = self.head
        if index >= self.size or index <0:
            return -1
        else:

            for i in range(index):
                q = q.next
            return(q.val)
        

        

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
        

        

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            q = self.head
            while q.next != None:
                q = q.next
            q.next = new_node
            self.size += 1



        

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return

        new_node = Node(val)

        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node

        self.size += 1
            




            
        

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            self.head = self.head.next 
        else:
            current = self.head
            for _ in range(index -1):
                current = current.next
            delete_node = current.next
            current.next = current.next.next
            delete_node.next = None
        self.size -= 1
        


        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)