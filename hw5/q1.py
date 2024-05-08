class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return (3 * key + 5) % self.size

    def insert(self, key):
        index = self.hash_function(key)
        node = Node(key)

        if self.table[index] is None:
            self.table[index] = node
        else:
            current = self.table[index]
            while current.next is not None:
                current = current.next
            current.next = node

    def print(self):
        for i in range(self.size):
            print(f"Index {i}: ", end="")
            current = self.table[i]
            while current is not None:
                print(f"{current.key} -> ", end="")
                current = current.next
            print("None")


hash_table = HashTable(11)


keys = [12, 44, 13, 88, 23, 94, 11, 39, 20, 16, 5]
for key in keys:
    hash_table.insert(key)


hash_table.print()