class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    # Convert array to linked list
    def array_to_linked_list(self, arr):
        if not arr:
            return
        self.head = Node(arr[0])
        current = self.head
        for item in arr[1:]:
            current.next = Node(item)
            current = current.next
    
    # Add a node at the beginning
    def add_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    # Add a node at the end
    def add_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    
    def delete_even_numbers(self):
        # Handle the head separately if it's an even number
        while self.head and self.head.data % 2 == 0:
            self.head = self.head.next

        current = self.head

        # Traverse the list and remove even numbers
        while current and current.next:
            if current.next.data % 2 == 0:
                current.next = current.next.next
            else:
                current = current.next
    
    # Delete a node with specified value
    def delete_node(self, key):
        current = self.head
        
        # If the node to be deleted is the head
        if current and current.data == key:
            self.head = current.next
            current = None
            return
        
        # Find the node to be deleted
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        
        if not current:
            print(f"Node with value {key} not found.")
            return
        
        # Unlink the node from the linked list
        prev.next = current.next
        current = None
    
    # Insert a node after a node with specified data
    def insert_after(self, prev_node_data, new_data):
        current = self.head
        while current and current.data != prev_node_data:
            current = current.next
        if not current:
            print(f"Node with value {prev_node_data} not found.")
            return
        new_node = Node(new_data)
        new_node.next = current.next
        current.next = new_node
    
    # Insert a node before a node with specified data
    def insert_before(self, next_node_data, new_data):
        if not self.head:
            print("List is empty.")
            return
        if self.head.data == next_node_data:
            new_node = Node(new_data)
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        prev = None
        while current and current.data != next_node_data:
            prev = current
            current = current.next
        if not current:
            print(f"Node with value {next_node_data} not found.")
            return
        new_node = Node(new_data)
        new_node.next = current
        prev.next = new_node
    
    # Print all elements in order
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
    
    # Helper function to print elements in reverse
    def _print_reverse(self, node):
        if not node:
            return
        self._print_reverse(node.next)
        print(node.data, end=" -> ")
    
    # Print all elements in reverse order
    def print_reverse_list(self):
        self._print_reverse(self.head)
        print("None")
    
    # Remove duplicates from a sorted list
    def remove_duplicates(self):
        current = self.head
        while current and current.next:
            if current.data == current.next.data:
                current.next = current.next.next
            else:
                current = current.next

    # Remove duplicates from a unsorted list
    def remove_duplicates(head):
        if not head:
            return None
        seen = set()
        curr = head
        seen.add(curr.val)
        while curr.next:
            if curr.next.val in seen:
                curr.next = curr.next.next
            else:
                seen.add(curr.next.val)
                curr = curr.next
        return head


    def find_middle(head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.val

        
    # Reverse the linked list
    def reverse_list(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

# Example usage
sll = SinglyLinkedList()

# Convert array to linked list
sll.array_to_linked_list([1, 1, 2, 3, 3, 2, 1,1])
sll.print_list()  # Output: 1 -> 1 -> 2 -> 3 -> 3 -> 4 -> 5 -> None


# Print all elements in reverse order
sll.print_reverse_list()  # Output: 6 <- 1 <- 2 <- 3.5 <- 3 <- 4 <- 5 <- 0 <- None
print(sll.is_palidrom())