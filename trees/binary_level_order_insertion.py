class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insert_level_order(arr):
    if not arr:
        return None
    
    root = TreeNode(arr[0])
    queue = collections.deque([root])
    i = 1
    
    while queue and i < len(arr):
        current = queue.popleft()
        
        if arr[i] is not None:
            current.left = TreeNode(arr[i])
            queue.append(current.left)
        i += 1
        
        if i < len(arr) and arr[i] is not None:
            current.right = TreeNode(arr[i])
            queue.append(current.right)
        i += 1
    
    return root

def level_order_traversal(root):
    if not root:
        return []
    
    result = []
    queue = collections.deque([root])
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(current_level)
    
    return result

# Example usage
if __name__ == "__main__":
    import collections
    
    # Input array with None for empty nodes
    arr = [1, 2, 3, 4, None, 6, 7, None, None, None, None, 12]
    
    # Build tree using level order insertion
    root = insert_level_order(arr)
    
    # Verify by doing level order traversal
    print("Level order traversal:")
    for level in level_order_traversal(root):
        print(level)