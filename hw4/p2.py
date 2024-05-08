class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def count_nodes(head):
    if head is None:
        return 0

    count = 1
    current = head.next
    while current != head:
        count += 1
        current = current.next

    return count

head = Node(1)
node2 = Node(2)
node3 = Node(3)
head.next = node2
node2.next = node3
node3.next = head
print(count_nodes(head))

OUTPUT:
3
