
tuple1 = ("green", "red", "blue")

tuple2 = (7, 1, 2, 23, 4, 5)

print("Length of tuple2:", len(tuple2))

print("Maximum value in tuple2:", max(tuple2))

print("Minimum value in tuple2:", min(tuple2))

print("Sum of tuple2 elements:", sum(tuple2))
tuple3 = tuple1 + tuple2
print("Tuple3:", tuple3)

tuple3 = tuple(x * 2 for x in tuple1)
print("Tuple3:", tuple3)


tuple3 = tuple2[2:4]
print("Tuple3:", tuple3)

print("Last element in tuple1:", tuple1[-1])

list_from_tuple2 = list(tuple2)
list_from_tuple2.sort()
tuple3 = tuple(list_from_tuple2)
print("New tuple from sorted list:", tuple3)
