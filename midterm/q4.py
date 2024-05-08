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
        if self.table[index] is None:
            self.table[index] = Node(key)
        else:
            current = self.table[index]
            while current.next is not None:
                current = current.next
            current.next = Node(key)

    def display(self):
        for i in range(self.size):
            print(f"{i}: ", end="")
            current = self.table[i]
            while current:
                print(f"[{current.key}]", end=" -> ")
                current = current.next
            print("None")

# Creating the hash table
keys = [12, 44, 13, 88, 23, 94, 11, 39, 20, 16, 5]
hash_table = HashTable(11)
for key in keys:
    hash_table.insert(key)

# Displaying the hash table
hash_table.display()
