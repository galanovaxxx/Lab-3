class Stack:
    """
    Класс Stack — стек на списке с поддержкой получения минимума за O(1).
    Использует два списка: основной для хранения элементов и вспомогательный для отслеживания минимума.
    """

    def __init__(self) -> None:
        self._items: list[int] = []  # основной список для хранения элементов стека
        self._mins: list[int] = []   # вспомогательный стек для отслеживания минимума

    @property
    def items(self) -> list[int]:
        """Возвращает копию текущего состояния стека (для вывода)."""
        return self._items.copy()

    def push(self, x: int) -> None:
        """Добавляет элемент x в стек и обновляет стек минимумов."""
        self._items.append(x)  # кладём элемент в основной стек
        if not self._mins or x <= self._mins[-1]:  # если стек минимумов пуст или x меньше текущего минимума
            self._mins.append(x)  # кладём x в стек минимумов
        else:
            self._mins.append(self._mins[-1])  # иначе повторяем предыдущий минимум

    def pop(self) -> int:
        """Удаляет и возвращает верхний элемент стека. Бросает IndexError, если стек пуст."""
        if self.is_empty():
            raise IndexError("pop from empty stack")  # если стек пуст — ошибка
        self._mins.pop()  # убираем верхний минимум
        return self._items.pop()  # убираем и возвращаем верхний элемент

    def peek(self) -> int:
        """Возвращает верхний элемент стека без удаления. Бросает IndexError, если стек пуст."""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]  # возвращаем верхний элемент

    def top(self) -> int:
        """Алиас для peek(). Возвращает верхний элемент стека."""
        return self.peek()

    def min(self) -> int:
        """Возвращает минимальный элемент стека за O(1). Бросает ValueError, если стек пуст."""
        if self.is_empty():
            raise ValueError("stack is empty")
        return self._mins[-1]  # верхний элемент стека минимумов — это минимум всего стека

    def is_empty(self) -> bool:
        """Проверяет, пуст ли стек."""
        return not self._items

    def __len__(self) -> int:
        """Возвращает количество элементов в стеке."""
        return len(self._items)