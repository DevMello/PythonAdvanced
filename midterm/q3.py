class Node(object):
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

class Tree(object):

    def insert(self, root, val):
        if root is None:
            root = Node(val=val)
            return root
        if root.val >= val:
            root.left = self.insert(root.left, val)
        elif root.val < val:
            root.right = self.insert(root.right, val)
        return root

    def next(self, root, number):
        traversal_sequence = []
        self.postorder(root, traversal_sequence)
        for i in range(len(traversal_sequence)):
            if traversal_sequence[i] == number:
                return traversal_sequence[i+1]
        return None

    def postorder(self, root, traversal_sequence):
        if root is not None:
            self.postorder(root.left, traversal_sequence)
            self.postorder(root.right, traversal_sequence)
            traversal_sequence.append(root.val)

    


root = None
binaryTree = Tree()
root = binaryTree.insert(root, 5)
binaryTree.insert(root, 3)
binaryTree.insert(root, 2)
binaryTree.insert(root, 4)
binaryTree.insert(root, 6)
next_node = binaryTree.next(root, 3)
print("Next Node:", next_node)


