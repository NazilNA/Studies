
class MinHeap:
    def __init__(self):
        self.heap = []
    def build_heap(self, array):
        self.heap = array                                    #[1,9, 5, 6, 2, 3] 2,0  l=5 r= 6 s =2    small = left
        for i in range(len(array) // 2 - 1, -1, -1):
            self._heapify_down(i)
    def _heapify_down(self, i):
        left = 2 * i + 1
        right = 2 * i + 2
        smallest = i
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left

        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self._heapify_down(smallest)

    def insert(self, key):
        self.heap.append(key)
        self._heapify_up(len(self.heap) - 1)
    def _heapify_up(self, i):
        parent = (i - 1) // 2
        if i > 0 and self.heap[i] < self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            self._heapify_up(parent)
    def remove(self):
        if len(self.heap) == 0:
            return None
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root
    


class MaxHeap():
    def __init__(self) :
        self.heap = []

    def build_heap(self,arr):
        self.heap = arr
        for i in range(len(arr)//2-1,-1,-1):
            self._heap_down(i)
    def _heap_down(self,i):
        left = 2*i+1
        right =2*i+2
        largest =  i
        
        if left < len(self.heap) and self.heap[left] >  self.heap[largest]:
            largest = left 

        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != i :
            self.heap[largest],self.heap[i] = self.heap[i],self.heap[largest]
            self._heap_down(largest)

    def insert(self,value):
        self.heap.append(value)
        self._heap_up(len(self.heap)-1)

    def _heap_up(self,i):
        parent = (i-1)//2
        
        if i>0 and self.heap[i]>self.heap[parent]:
            self.heap[parent],self.heap[i]=self.heap[i],self.heap[parent]
            self._heap_up(parent)
            







min_heap = MinHeap()
min_heap.build_heap([9, 5, 6, 2, 3])
min_heap.insert(1)
print("Min-Heap before removal:", min_heap.heap)
removed_element = min_heap.remove()
print("Removed element:", removed_element)
print("Min-Heap after removal:", min_heap.heap)