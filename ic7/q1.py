class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def sorted_array_to_bst(nums):
    if not nums:
        return None

    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    root.left = sorted_array_to_bst(nums[:mid])
    root.right = sorted_array_to_bst(nums[mid+1:])
    return root

def preOrder(node):
    if not node:
        return
    print(node.val)
    preOrder(node.left)
    preOrder(node.right)

result = sorted_array_to_bst([1, 2, 3, 4, 5, 6, 7])
preOrder(result)