import pytest

from src.factorial_fibo import factorial, factorial_recursive, fibo, fibo_recursive
from src.generation import rand_int_array, rand_float_array, reverse_sorted, many_duplicates
from src.queue import Queue
from src.sorts import (
    bubble_sort, quick_sort, counting_sort,
    radix_sort, heap_sort, shell_sort, bucket_sort,
)
from src.sorting_utils import bubble_sort as bubble_key, quick_sort as quick_key
from src.stack import Stack


# факториал и фибоначчи

def test_factorial():
    """Факториал — корректные значения."""
    assert factorial(0) == 1
    assert factorial(5) == 120
    assert factorial_recursive(5) == 120


def test_factorial_errors():
    """Факториал — ошибки."""
    with pytest.raises(ValueError):
        factorial(-1)
    with pytest.raises(ValueError):
        factorial(2.5)


def test_fibo():
    """Фибоначчи — корректные значения."""
    assert fibo(0) == 0
    assert fibo(6) == 8
    assert fibo_recursive(6) == 8


def test_fibo_errors():
    """Фибоначчи — ошибки."""
    with pytest.raises(ValueError):
        fibo(-1)
    with pytest.raises(ValueError):
        fibo(3.5)


# сортировки

def test_bubble_sort():
    """Пузырьковая сортировка."""
    data = rand_int_array(25, -100, 100, seed=1)
    expected = sorted(data)
    bubble_sort(data)
    assert data == expected


def test_quick_sort():
    """Быстрая сортировка."""
    data = rand_int_array(25, -100, 100, seed=2)
    expected = sorted(data)
    quick_sort(data)
    assert data == expected


def test_counting_sort():
    """Сортировка подсчётом."""
    data = rand_int_array(25, -50, 50, seed=3)
    expected = sorted(data)
    counting_sort(data)
    assert data == expected


def test_radix_sort():
    """Поразрядная сортировка."""
    data = rand_int_array(25, -100, 100, seed=4)
    expected = sorted(data)
    radix_sort(data)
    assert data == expected


def test_heap_sort():
    """Пирамидальная сортировка."""
    data = rand_int_array(25, -100, 100, seed=5)
    expected = sorted(data)
    heap_sort(data)
    assert data == expected


def test_shell_sort():
    """Сортировка Шелла."""
    data = rand_int_array(25, -100, 100, seed=6)
    expected = sorted(data)
    shell_sort(data)
    assert data == expected


def test_bucket_sort():
    """Блочная сортировка float."""
    data = rand_float_array(25, 0.0, 1.0, seed=7)
    expected = sorted(data)
    bucket_sort(data)
    assert data == expected


def test_sorts_edge_cases():
    """Сортировки — граничные случаи."""
    assert bubble_sort([]) == []
    assert quick_sort([42]) == [42]
    data = reverse_sorted(15)
    expected = sorted(data)
    heap_sort(data)
    assert data == expected


def test_sorts_duplicates():
    """Сортировки — массив с дубликатами."""
    data = many_duplicates(25, k_unique=4, seed=8)
    expected = sorted(data)
    quick_sort(data)
    assert data == expected


# сортировки с ключом

def test_sort_key_len():
    """Сортировка по длине строки."""
    data = ["banana", "pie", "apple", "a"]
    expected = sorted(data, key=len)
    bubble_key(data, key=len)
    assert data == expected


def test_sort_cmp_reverse():
    """Сортировка с компаратором по убыванию."""
    data = rand_int_array(15, 1, 50, seed=9)
    expected = sorted(data, reverse=True)
    cmp_desc = lambda a, b: -1 if a > b else (1 if a < b else 0)
    quick_key(data, cmp=cmp_desc)
    assert data == expected


# стек

def test_stack_operations():
    """Стек — основные операции."""
    s = Stack()
    s.push(5)
    s.push(3)
    s.push(7)
    assert s.peek() == 7
    assert s.top() == 7
    assert s.min() == 3
    assert s.pop() == 7
    assert len(s) == 2
    assert not s.is_empty()


def test_stack_errors():
    """Стек — ошибки при пустом стеке."""
    s = Stack()
    with pytest.raises(IndexError):
        s.pop()
    with pytest.raises(IndexError):
        s.peek()
    with pytest.raises(ValueError):
        s.min()


# очередь

def test_queue_operations():
    """Очередь — основные операции."""
    q = Queue()
    q.enqueue("A")
    q.enqueue("B")
    assert q.front() == "A"
    assert q.dequeue() == "A"
    assert len(q) == 1
    assert not q.is_empty()


def test_queue_errors():
    """Очередь — ошибки при пустой очереди."""
    q = Queue()
    with pytest.raises(IndexError):
        q.dequeue()
    with pytest.raises(IndexError):
        q.front()


# генерация

def test_generation():
    """Генерация тест-кейсов."""
    arr = rand_int_array(10, 1, 100, seed=10)
    assert len(arr) == 10
    assert all(1 <= x <= 100 for x in arr)

    floats = rand_float_array(10, 0.0, 1.0, seed=11)
    assert all(0.0 <= x <= 1.0 for x in floats)

    assert reverse_sorted(5) == [5, 4, 3, 2, 1]


def test_generation_distinct_error():
    """Генерация — ошибка при невозможности создать уникальные."""
    with pytest.raises(ValueError):
        rand_int_array(10, 1, 5, distinct=True)
