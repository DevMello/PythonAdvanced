elements = ['a', 'b', 'c', 'd', 'e', 'f']

def move_to_front(lst, index):
    element = lst.pop(index)
    lst.insert(0, element)


access_sequence = ['a', 'b', 'c', 'd', 'e', 'f', 'a', 'c', 'f', 'b', 'd', 'e']

for element in access_sequence:
    if element in elements:
        index = elements.index(element)
        move_to_front(elements, index)
    print(elements)

OUTPUT:

['a', 'b', 'c', 'd', 'e', 'f']
['b', 'a', 'c', 'd', 'e', 'f']
['c', 'b', 'a', 'd', 'e', 'f']
['d', 'c', 'b', 'a', 'e', 'f']
['e', 'd', 'c', 'b', 'a', 'f']
['f', 'e', 'd', 'c', 'b', 'a']
['a', 'f', 'e', 'd', 'c', 'b']
['c', 'a', 'f', 'e', 'd', 'b']
['f', 'c', 'a', 'e', 'd', 'b']
['b', 'f', 'c', 'a', 'e', 'd']
['d', 'b', 'f', 'c', 'a', 'e']
['e', 'd', 'b', 'f', 'c', 'a']