class NaryTreeNode:
    def __init__(self, value):
        self.value = value  # The value stored in the node
        self.children = []  # List to store children nodes

class NaryTree:
    def __init__(self):
        self.root = None  # Initialize the tree with no root

    def set_root(self, value):
        self.root = NaryTreeNode(value)  # Set the root of the tree

    def add_child(self, parent_value, child_value):
        parent = self._find(self.root, parent_value)
        if parent:
            parent.children.append(NaryTreeNode(child_value))
        else:
            print(f"Parent {parent_value} not found.")

    def _find(self, node, value):
        if node is None:
            return None
        if node.value == value:
            return node
        for child in node.children:
            found = self._find(child, value)
            if found:
                return found
        return None
    
    def inorder_traversal(self, node):
        if node:
            mid = len(node.children) // 2
            for child in node.children[:mid]:
                self.inorder_traversal(child)
            print(node.value, end=' ')
            for child in node.children[mid:]:
                self.inorder_traversal(child)

    
                
    def preorder_traversal(self, node):
        if node:
            print(node.value, end=' ')
            for child in node.children:
                self.preorder_traversal(child)

    def postorder_traversal(self, node):
        if node:
            for child in node.children:
                self.postorder_traversal(child)
            print(node.value, end=' ')

tree = NaryTree()

tree.set_root(1)
tree.add_child(1, 2)
tree.add_child(1, 3)
tree.add_child(1, 4)
tree.add_child(2, 5)
tree.add_child(2, 6)

print("Preorder traversal: ", end='')
tree.preorder_traversal(tree.root)  
print("\nPostorder traversal: ", end='')
tree.postorder_traversal(tree.root)
