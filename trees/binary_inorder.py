class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal_recursive(root):
    """Recursive inorder traversal"""
    result = []
    
    def traverse(node):
        if node:
            traverse(node.left)      # Visit left subtree
            result.append(node.val)  # Visit node
            traverse(node.right)     # Visit right subtree
    
    traverse(root)
    return result