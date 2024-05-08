import time
from llist import sllist

start_time = time.time()

linked_list = sllist()

for i in range(1, 1001):
    linked_list.append(i)

elapsed_time = time.time() - start_time

print("LinkedList: ", list(linked_list))
print("Time for LinkedList populating is", elapsed_time, "seconds")

start_time = time.time()

for i in range(1, 1001):
    linked_list.pop()

elapsed_time = time.time() - start_time

print("Time for LinkedList popping is", elapsed_time, "seconds")

start_time = time.time()
