class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, x):
        """Добавить в конец"""
        self.items.append(x)

    def dequeue(self):
        """Удалить из начала"""
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def front(self):
        """Посмотреть первый элемент"""
        if not self.is_empty():
            return self.items[0]
        return None

    def is_empty(self):
        return len(self.items) == 0

queue = Queue()
queue.enqueue('A')
queue.enqueue('B')
queue.enqueue('C')

print(queue.items)     # ['A', 'B', 'C']
print(queue.dequeue()) # 'A'
print(queue.items)     # ['B', 'C']