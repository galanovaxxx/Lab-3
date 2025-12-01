# Лабораторная работа №3  **Тема:** Алгоритмический мини-пакет 

## Автор

### Галанова Екатерина Алексеевна группа М8О-102БВ-25

## Структура проекта

```
Lab-3/
├── src/
│   ├── main.py              # Точка входа (CLI)
│   ├── factorial_fibo.py    # Факториал и числа Фибоначчи
│   ├── sorts.py             # Базовые сортировки
│   ├── sorting_utils.py     # Сортировки с поддержкой key и cmp
│   ├── stack.py             # Стек с получением минимума за O(1)
│   ├── queue.py             # Очередь FIFO
│   ├── generation.py        # Генерация тест-кейсов
│   └── benchmark.py         # Бенчмарк сортировок
├── tests/
│   └── test_lab3.py         # Unit-тесты
├── requirements.txt
├── pyproject.toml
└── README.md
```

## Реализованный функционал

### 1. Факториал и Фибоначчи

```python
def factorial(n: int) -> int           # итеративный факториал
def factorial_recursive(n: int) -> int # рекурсивный факториал
def fibo(n: int) -> int                # итеративное число Фибоначчи
def fibo_recursive(n: int) -> int      # рекурсивное число Фибоначчи
```

### 2. Сортировки

**Базовые (sorts.py):**
```python
def bubble_sort(a: list[int]) -> list[int]                    # пузырьком
def quick_sort(a: list[int]) -> list[int]                     # быстрая
def counting_sort(a: list[int]) -> list[int]                  # подсчётом
def radix_sort(a: list[int], base: int = 10) -> list[int]     # поразрядная
def bucket_sort(a: list[float], buckets: int | None) -> list[float]  # блочная
def heap_sort(a: list[int]) -> list[int]                      # пирамидальная
def shell_sort(a: list[int]) -> list[int]                     # Шелла
```

**С поддержкой key и cmp (sorting_utils.py):**
```python
def bubble_sort(a: list[T], key=None, cmp=None) -> list[T]
def quick_sort(a: list[T], key=None, cmp=None) -> list[T]
def heap_sort(a: list[T], key=None, cmp=None) -> list[T]
def shell_sort(a: list[T], key=None, cmp=None) -> list[T]
def counting_sort(a: list[T], key=None) -> list[T]
def radix_sort(a: list[T], base=10, key=None) -> list[T]
def bucket_sort(a: list[T], buckets=None, key=None) -> list[T]
```

### 3. Структуры данных

**Стек (на списке с O(1) минимумом):**
```python
class Stack:
    def push(self, x: int) -> None      # добавить элемент
    def pop(self) -> int                # извлечь элемент (IndexError если пуст)
    def peek(self) -> int               # посмотреть вершину (IndexError если пуст)
    def top(self) -> int                # алиас для peek()
    def min(self) -> int                # минимум за O(1) (ValueError если пуст)
    def is_empty(self) -> bool          # проверка на пустоту
    def __len__(self) -> int            # количество элементов
```

**Очередь (FIFO на списке):**
```python
class Queue:
    def enqueue(self, x: int) -> None   # добавить в конец
    def dequeue(self) -> int            # извлечь из начала (IndexError если пуста)
    def front(self) -> int              # посмотреть первый (IndexError если пуста)
    def is_empty(self) -> bool          # проверка на пустоту
    def __len__(self) -> int            # количество элементов
```

### 4. Генерация тест-кейсов

```python
def rand_int_array(n, lo, hi, distinct=False, seed=None) -> list[int]
def rand_float_array(n, lo=0.0, hi=10.0, seed=None) -> list[float]
def reverse_sorted(n) -> list[int]         # [n, n-1, ..., 1]
def nearly_sorted(n, swaps, seed=None) -> list[int]
def many_duplicates(n, k_unique=5, seed=None) -> list[int]
```

### 5. Бенчмарк

```python
def timeit_once(func, *args, **kwargs) -> float
def benchmark_sorts(arrays, algos) -> dict[str, dict[str, float]]
def print_benchmark_table(results)
```

## Использование CLI

Запуск:
```bash
cd src
python main.py
```

**Команды:**

```
fact 5                    → 120 (факториал)
fact_r 5                  → 120 (рекурсивный)
fibo 6                    → 8 (Фибоначчи)
fibo_r 6                  → 8 (рекурсивный)

bubble 5 2 8 1 9          → [1, 2, 5, 8, 9]
quick 5 2 8 1 9           → [1, 2, 5, 8, 9]
counting 5 2 8 1 9        → [1, 2, 5, 8, 9]
radix 5 2 8 1 9           → [1, 2, 5, 8, 9]
heap 5 2 8 1 9            → [1, 2, 5, 8, 9]
shell 5 2 8 1 9           → [1, 2, 5, 8, 9]
bucket 0.5 0.2 0.8        → [0.2, 0.5, 0.8]

bubble_key len apple pie a      → ['a', 'pie', 'apple']
quick_key neg 5 2 8 1           → [8, 5, 2, 1]
bubble_cmp 5 2 8 1              → [8, 5, 2, 1]

stack push 5              → pushed 5
stack pop                 → 5
stack min                 → минимум
stack show                → содержимое стека

queue enq hello           → enqueued hello
queue deq                 → hello
queue show                → содержимое очереди

exit                      → выход
```

## Запуск тестов

```bash
pytest tests/test_lab3.py -v
```

## Ограничения

- Запрещено использовать `list.sort()` и `sorted()` в реализации сортировок
- Разрешена стандартная библиотека
- Для Medium разрешён `functools.cmp_to_key`
- Bucket sort по умолчанию работает с float (с нормализацией)
- Структуры данных выбрасывают исключения при некорректных операциях


