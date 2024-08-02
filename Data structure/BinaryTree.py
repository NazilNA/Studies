'''
||Binary Tree||'''

class BinaryTreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_left(self, parent, key):
        parent.left = BinaryTreeNode(key)

    def insert_right(self, parent, key):
        parent.right = BinaryTreeNode(key)

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.key, end=' ')
            self.inorder_traversal(node.right)

    def preorder_traversal(self, node):
        if node:
            print(node.key, end=' ')
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)

    def postorder_traversal(self, node):
        if node:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.key, end=' ')
# Example usage
bt = BinaryTree()
bt.root= BinaryTreeNode(1)
bt.insert_left(bt.root, 2)
bt.insert_right(bt.root, 3)
bt.insert_left(bt.root.left, 4)
bt.insert_right(bt.root.left, 5)

print("Inorder traversal of binary tree:")
bt.inorder_traversal(bt.root) 
print("\nPre-order Traversal:")
bt.preorder_traversal(bt.root)
print("\nPost-order Traversal:")
bt.postorder_traversal(bt.root) 

