class Node:
    # Singly linked node
    def __init__(self, data=None):
        self.data = data
        self.next = None

class singly_linked_list:
    def __init__(self):
        # Create an empty list
        self.tail = None
        self.head = None
        self.count = 0

    def append_item(self, data):
        # Append items to the list
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.count += 1

    def search_item(self, val):
        # Search the list one node at a time and check if it has the desired value
        current = self.head
        while current:
            if current.data == val:
                return True
            current = current.next
        return False

items = singly_linked_list()
items.append_item('PHP')
items.append_item('Python')
items.append_item('C#')
items.append_item('C++')
items.append_item('Java')

if items.search_item('SQL'):
    print("True")
else:
    print("False")

if items.search_item('C++'):
    print("True")
else:
    print("False")