

from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    

def createTreeByLevel(arr):
    if not arr:
        return None
    
    root = TreeNode(arr[0]) 
    queue = deque([root])

    i = 1

    while i < len(arr):
        node = queue.popleft()
        
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        
        i += 1

        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)

        i += 1

    return root






def maxDepth(root):
    if not root:
        return 0
    
    return 1 + max(maxDepth(root.left), maxDepth(root.right))


tree = [3,9,20, None, None,15,7]

root = createTreeByLevel(tree)

print(maxDepth(root))


    