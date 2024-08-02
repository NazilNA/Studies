class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def delete(self, word):
        def _delete(node, word, depth):
            if not node:
                return False

            if depth == len(word):
                if not node.is_end_of_word:
                    return False
                node.is_end_of_word = False
                return len(node.children) == 0  # If true, delete this node

            char = word[depth]
            if char in node.children and _delete(node.children[char], word, depth + 1):
                del node.children[char]
                return len(node.children) == 0 and not node.is_end_of_word

            return False
        
        _delete(self.root, word, 0)
        

    def print_trie(self):
        def _print(node, current_word):
            # If this node marks the end of a word, print the word accumulated so far.
            if node.is_end_of_word:
                print(current_word)

            # Iterate through all the children of the current node.
            for char, child_node in node.children.items():
                # Call _print recursively for each child, adding the child's character to the current word.
                _print(child_node, current_word + char)
        
        # Start the recursive printing process from the root node with an empty string.
        _print(self.root, "")

# Example usage:
trie = Trie()
trie.insert("bat")
trie.insert("ball")
trie.insert("bark")

# Deleting the word "ball"
trie.delete("apple")

# Printing all words in the Trie
print("Words in the Trie after deletion:")
trie.print_trie()

# Checking if any words start with "ba"
print("\nDoes any word start with 'ba'?")
print(trie.starts_with("ba"))  # Should return True

# Searching for the word "ball"
print("\nIs 'ball' in the Trie?")
print(trie.search("ball"))  # Should return False
