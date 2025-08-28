class Node:
    def __init__(self, data, color='R'):
        self.data = data
        self.color = color  # 'R' for Red, 'B' for Black
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.NIL = Node(0, 'B')  # Sentinel node
        self.root = self.NIL
    
    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        
        if y.left != self.NIL:
            y.left.parent = x
        
        y.parent = x.parent
        
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        
        y.left = x
        x.parent = y
    
    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        
        if y.right != self.NIL:
            y.right.parent = x
        
        y.parent = x.parent
        
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        
        y.right = x
        x.parent = y
    
    def fix_insert(self, k):
        while k.parent and k.parent.color == 'R':
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left  # uncle
                if u.color == 'R':
                    u.color = 'B'
                    k.parent.color = 'B'
                    k.parent.parent.color = 'R'
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = 'B'
                    k.parent.parent.color = 'R'
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right  # uncle
                if u.color == 'R':
                    u.color = 'B'
                    k.parent.color = 'B'
                    k.parent.parent.color = 'R'
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = 'B'
                    k.parent.parent.color = 'R'
                    self.right_rotate(k.parent.parent)
            
            if k == self.root:
                break
        
        self.root.color = 'B'
    
    def insert(self, key):
        node = Node(key)
        node.parent = None
        node.data = key
        node.left = self.NIL
        node.right = self.NIL
        node.color = 'R'  # New node is always red
        
        y = None
        x = self.root
        
        while x != self.NIL:
            y = x
            if node.data < x.data:
                x = x.left
            else:
                x = x.right
        
        node.parent = y
        if y is None:
            self.root = node
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node
        
        if node.parent is None:
            node.color = 'B'
            return
        
        if node.parent.parent is None:
            return
        
        self.fix_insert(node)
    
    def print_tree(self, node, indent="", last=True):
        if node != self.NIL:
            print(indent, end="")
            if last:
                print("└── ", end="")
                indent += "    "
            else:
                print("├── ", end="")
                indent += "│   "
            
            color_char = 'B' if node.color == 'B' else 'R'
            print(f"{node.data}({color_char})")
            
            self.print_tree(node.left, indent, False)
            self.print_tree(node.right, indent, True)
    
    def display_tree(self):
        print("\nRed-Black Tree Structure:")
        self.print_tree(self.root)

def main():
    rbt = RedBlackTree()
    
    print("Red-Black Tree Insertion")
    print("Enter numbers to insert (space separated):")
    
    try:
        user_input = input().split()
        numbers = [int(num) for num in user_input]
        
        for num in numbers:
            rbt.insert(num)
            print(f"Inserted: {num}")
        
        rbt.display_tree()
        
    except ValueError:
        print("Please enter valid integers only!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()