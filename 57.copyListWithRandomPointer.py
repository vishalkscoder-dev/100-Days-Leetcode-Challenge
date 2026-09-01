import os
os.system('cls')

class Node:
    def __init__(self,val=0,next=None,random=None):
        self.val = val
        self.next = next
        self.random = random

def copyListRandomPointer(head):
    oldToNew = {}

    current = head

    while current:
        oldToNew[current] = Node(current.val)
        current = current.next

    current = head

    while current:
        copy = oldToNew[current]
        copy.next = oldToNew.get(current.next)
        copy.random = oldToNew.get(current.random)

        current = current.next

    return oldToNew[head]

node1 = Node(7)
node2 = Node(13)
node3 = Node(11)
node4 = Node(10)
node5 = Node(1)


node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

node1.random = None
node2.random = node1
node3.random = node5
node4.random = node3
node5.random = node1


head = node1

copyHead = copyListRandomPointer(head)

current = copyHead

while current:
    random = current.random.val if current.random else None

    print([current.val, random])

    current = current.next


