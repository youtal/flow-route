class PriorityQueue:
    def __init__(self):
        self.queue = []
        self.size = 0

    def swap(self, i, j):
        self.queue[i], self.queue[j] = self.queue[j], self.queue[i]

    def shift_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self.queue[i]['priority'] < self.queue[parent]['priority']:
                self.swap(i, parent)
                i = parent
            else:
                break

    def shift_down(self, i):
        while i * 2 + 1 < self.size:
            left = i * 2 + 1
            right = i * 2 + 2
            min_index = left
            if right < self.size and self.queue[right]['priority'] < self.queue[left]['priority']:
                min_index = right
            if self.queue[i]['priority'] > self.queue[min_index]['priority']:
                self.swap(i, min_index)
                i = min_index
            else:
                break

    def enqueue(self, val):
        self.queue.append(val)
        self.size += 1
        self.shift_up(self.size - 1)

    def dequeue(self):
        if self.size == 0:
            return None
        self.swap(0, self.size - 1)
        self.size -= 1
        self.shift_down(0)
        return self.queue.pop()

    def is_empty(self):
        return self.size == 0
