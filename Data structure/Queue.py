class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, item):
        self.queue.append(item)
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
    def peek(self):
        if not self.is_empty():
            return self.queue[0]
    def is_empty(self):
        return len(self.queue) == 0
def find_max_element(queue):
    if queue.is_empty():
        return None
    max_element = queue.peek()
    for item in queue.queue:
        if item > max_element:
            max_element = item
    return max_element
q = Queue()
q.enqueue(5)
q.enqueue(2)
q.enqueue(8)
q.enqueue(3)
print("Maximum element in the queue:", find_max_element(q))
