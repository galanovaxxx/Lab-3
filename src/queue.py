class Queue:
    """
    Класс Queue — очередь FIFO на списке с использованием pop(0).
    FIFO (first-in, first-out): элементы извлекаются в порядке добавления.
    """

    def __init__(self) -> None:
        self._items = []  # основной список для хранения элементов очереди

    @property
    def items(self):
        """Возвращает копию очереди."""
        return self._items.copy()

    def enqueue(self, x) -> None:
        """Добавляет элемент x в конец очереди."""
        self._items.append(x)

    def dequeue(self):
        """Удаляет и возвращает элемент из начала очереди. Бросает IndexError, если очередь пуста."""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._items.pop(0)

    def front(self):
        """Возвращает первый элемент очереди без удаления. Бросает IndexError, если очередь пуста."""
        if self.is_empty():
            raise IndexError("front from empty queue")
        return self._items[0]

    def is_empty(self) -> bool:
        """Проверяет, пуста ли очередь."""
        return len(self._items) == 0

    def __len__(self) -> int:
        """Возвращает количество элементов в очереди."""
        return len(self._items)