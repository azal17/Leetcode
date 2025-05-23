# Iterative O(n) both.
def rr(head):
    q = head
    arr = []
    while q:
        arr.append(q.val)
        q = q.next
    arr = arr[::-1]
    print(arr)

# Recursion O(n) both (uses stack).
def rr1(head):
    if head == None:
        return
    rr1(head.next)
    print(head.val)

# Stack implementation, O(n) both.
def rr2(head):
    stack = []
    q = head
    while q:
        stack.append(q.val)
        q = q.next
    while stack:
        print(stack.pop())
