class Stack:
    def __init__(self):
        self.items = []

    def push(self, x):
        """Добавить элемент"""
        self.items.append(x)

    def pop(self):
        """Удалить и вернуть верхний элемент"""
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        """Посмотреть верхний элемент"""
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        """Проверка на пустоту"""
        return len(self.items) == 0


stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print(stack.items)  # [10, 20, 30]
print(stack.pop())  # 30
print(stack.pop())  # 20
print(stack.items)  # [10]