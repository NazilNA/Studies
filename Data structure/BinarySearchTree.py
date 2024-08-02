class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert_recursive(node.left, key)
        elif key > node.key:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert_recursive(node.right, key)

    def contains(self, key):
        return self._contains_recursive(self.root, key)

    def _contains_recursive(self, node, key):
        if node is None:
            return False
        if key == node.key:
            return True
        elif key < node.key:
            return self._contains_recursive(node.left, key)
        else:
            return self._contains_recursive(node.right, key)

    
    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def find_closest_value(self, target):
        return self._find_closest_value_recursive(self.root, target, float('inf'))

    def _find_closest_value_recursive(self, node, target, closest):
        if node is None:
            return closest
        
        if abs(node.key - target) < abs(closest - target):
            closest = node.key
         
        if target < node.key:
            return self._find_closest_value_recursive(node.left, target, closest)
        elif target > node.key:
            return self._find_closest_value_recursive(node.right, target, closest)
        else:
            return closest
        
    def is_bst(self):
        return self._is_bst_recursive(self.root, float('-inf'), float('inf'))

    def _is_bst_recursive(self, node, min_val, max_val):
        if not node:
            return True
        
        if node.key < min_val or node.key > max_val:
            return False
        
        return (self._is_bst_recursive(node.left, min_val, node.key) and
                self._is_bst_recursive(node.right, node.key, max_val))
    
    def delete(self,key):
        self.root = self.delete_recursive(self.root,key)
    
    def delete_recursive(self,root,key):
        if root is None:
            return root
        
        if key < root.key :
            root.left = self.delete_recursive(root.left,key)
        elif key > root.key :
            root.right = self.delete_recursive(root.right,key)

        else:
            if root.left is None:
                return root.right 
            if root.right is None:
                return root.left
            

            current = root.right 
            while current.left:
                current = current.left
            
            root.key = current.key
            root.right = self.delete_recursive(root.right,current.key)
        
        return root

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.key, end=' ')
            self.inorder_traversal(node.right)


# Example usage
bst = BinarySearchTree()
keys = [50, 30, 20, 40, 70, 60, 80]
for key in keys:
    bst.insert(key)

print("Inorder traversal of BST:")
bst.inorder_traversal(bst.root)  # Output: 20 30 40 50 60 70 80

print("\nIs valid BST:", bst.is_bst())  # Output: True
target_number = 65
closest_value = bst.find_closest_value(target_number)
print(f"Closest value to {target_number} is {closest_value}")  
print("Contains 40:", bst.contains(40))  # Output: True
print("Contains 100:", bst.contains(100))  # Output: False
bst.delete(50)
print("Inorder traversal after deleting 20:")
bst.inorder_traversal(bst.root) 
bst.second_larg_small()
