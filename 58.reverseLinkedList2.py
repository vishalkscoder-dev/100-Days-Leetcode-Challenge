import os
os.system('cls')

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseBetween(head, left, right):
    if not head or left == right:
        return head

    dummy = ListNode(0)
    dummy.next = head

    prev = dummy

    for i in range(left - 1):
        prev = prev.next

    current = prev.next

    for i in range(right - left):
        next_node = current.next
        current.next = next_node.next
        next_node.next = prev.next
        prev.next = next_node

    return dummy.next


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

result = reverseBetween(head, 2, 4)

current = result

while current:
    print(current.val, end=" -> ")
    current = current.next

print("None")