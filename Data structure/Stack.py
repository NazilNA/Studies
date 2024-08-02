'''class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
    def is_empty(self):
        return len(self.stack) == 0
    def size(self):
        return len(self.stack)
# Create a stack
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print("Top of the stack:", stack.peek())
print("Popped item:", stack.pop())
print("Popped item:", stack.pop())
print("Is the stack empty?", stack.is_empty())
print("Size of the stack:", stack.size())
'''


'''class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
    def is_empty(self):
        return len(self.stack) == 0
def reverse_string(input_str):
    stack = Stack()
    reversed_str = ""
    for char in input_str:
        stack.push(char)
    while not stack.is_empty():
        reversed_str += stack.pop()
    return reversed_str

input_str = "hello"
print("Input:", input_str)
print("Output:", reverse_string(input_str))
'''




'''

class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
    def is_empty(self):
        return len(self.stack) == 0
def reverse_words(sentence):
    stack = Stack()
    words = sentence.split()
    for word in words:
        stack.push(word)
    reversed_sentence = ""
    while not stack.is_empty():
        reversed_sentence += stack.pop() + " "

    return reversed_sentence.strip()
sentence = "hello world"
print("Input:", sentence)
print("Output:", reverse_words(sentence))
'''