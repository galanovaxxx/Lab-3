import random
from typing import TypeVar, Callable, Optional, Any

T = TypeVar('T')


def bubble_sort(a: list[T],
                key: Optional[Callable[[T], Any]] = None,
                cmp: Optional[Callable[[Any, Any], int]] = None) -> list[T]:
    """Сортировка пузырьком с поддержкой key и cmp."""
    n = len(a)  # длина массива

    def compare(x, y):
        """Сравнивает два элемента."""
        key_x = key(x) if key else x  # получаем ключ первого элемента
        key_y = key(y) if key else y  # получаем ключ второго элемента
        if cmp:
            return cmp(key_x, key_y) > 0  # используем компаратор
        return key_x > key_y  # стандартное сравнение

    for i in range(n):  # внешний цикл по всем элементам
        swapped = False  # флаг для оптимизации
        for j in range(n - i - 1):  # внутренний цикл до неотсортированной части
            if compare(a[j], a[j + 1]):  # если текущий больше следующего
                a[j], a[j + 1] = a[j + 1], a[j]  # меняем местами
                swapped = True  # был обмен
        if not swapped:  # если не было обменов — массив уже отсортирован
            break
    return a  # возвращаем отсортированный массив


def quick_sort(a: list[T],
               key: Optional[Callable[[T], Any]] = None,
               cmp: Optional[Callable[[Any, Any], int]] = None) -> list[T]:
    """Быстрая сортировка с поддержкой key и cmp."""
    if len(a) <= 1:
        return a  # базовый случай: массив из 0 или 1 элемента

    pivot = random.choice(a)  # выбираем случайный опорный элемент
    pivot_key = key(pivot) if key else pivot  # ключ опорного элемента

    def compare_val(x_key):
        """Сравнивает ключ с опорным."""
        if cmp:
            return cmp(x_key, pivot_key)  # используем компаратор
        if x_key < pivot_key:
            return -1
        elif x_key > pivot_key:
            return 1
        return 0

    lower = []  # элементы меньше опорного
    equal = []  # равные опорному
    higher = []  # больше опорного

    for x in a:
        x_key = key(x) if key else x  # получаем ключ элемента
        result = compare_val(x_key)
        if result < 0:
            lower.append(x)
        elif result == 0:
            equal.append(x)
        else:
            higher.append(x)

    sorted_result = quick_sort(lower, key, cmp) + equal + quick_sort(higher, key, cmp)  # рекурсивно сортируем
    a[:] = sorted_result  # копируем результат обратно в исходный массив
    return a


def counting_sort(a: list[T],
                  key: Optional[Callable[[T], int]] = None) -> list[T]:
    """Сортировка подсчётом с поддержкой key."""
    if not a:
        return []  # пустой массив

    keys = [key(x) if key else x for x in a]  # получаем ключи всех элементов
    min_val = min(keys)  # минимальное значение
    max_val = max(keys)  # максимальное значение
    range_size = max_val - min_val + 1  # диапазон значений

    count = [0] * range_size  # массив для подсчёта количества каждого значения
    output = [None] * len(a)  # выходной массив

    for x in a:
        k = key(x) if key else x  # получаем ключ
        count[k - min_val] += 1  # увеличиваем счётчик

    for i in range(1, len(count)):
        count[i] += count[i - 1]  # делаем массив накопительным

    for x in reversed(a):  # идём с конца для устойчивости
        k = key(x) if key else x
        idx = k - min_val
        count[idx] -= 1
        output[count[idx]] = x

    a[:] = output  # копируем результат обратно
    return a


def radix_sort(a: list[T],
               base: int = 10,
               key: Optional[Callable[[T], int]] = None) -> list[T]:
    """Поразрядная сортировка с поддержкой key."""
    def _radix_non_negative(nums: list[T], keys: list[int]) -> tuple[list[T], list[int]]:
        """Сортирует неотрицательные числа."""
        if not nums:
            return [], []

        exp = 1  # текущий разряд
        max_val = max(keys)  # максимальное значение ключа
        result = list(nums)  # копия элементов
        result_keys = list(keys)  # копия ключей

        while max_val // exp > 0:
            buckets = [[] for _ in range(base)]  # корзины для элементов
            key_buckets = [[] for _ in range(base)]  # корзины для ключей

            for i, num in enumerate(result):
                digit = (result_keys[i] // exp) % base  # выделяем цифру
                buckets[digit].append(num)
                key_buckets[digit].append(result_keys[i])

            result = [num for bucket in buckets for num in bucket]  # собираем обратно
            result_keys = [k for bucket in key_buckets for k in bucket]
            exp *= base  # переходим к следующему разряду

        return result, result_keys

    if not a:
        return []

    keys = [key(x) if key else x for x in a]  # получаем ключи

    # разделяем на положительные и отрицательные
    pos_items = [(x, k) for x, k in zip(a, keys) if k >= 0]
    neg_items = [(x, -k) for x, k in zip(a, keys) if k < 0]

    pos_nums = [x for x, k in pos_items]  # положительные элементы
    pos_keys = [k for x, k in pos_items]  # их ключи
    neg_nums = [x for x, k in neg_items]  # отрицательные элементы
    neg_keys = [k for x, k in neg_items]  # их ключи (по модулю)

    sorted_pos, _ = _radix_non_negative(pos_nums, pos_keys)  # сортируем положительные
    sorted_neg, _ = _radix_non_negative(neg_nums, neg_keys)  # сортируем отрицательные

    result = list(reversed(sorted_neg)) + sorted_pos  # собираем итог
    a[:] = result
    return a


def bucket_sort(a: list[T],
                buckets: int | None = None,
                key: Optional[Callable[[T], float]] = None) -> list[T]:
    """Блочная сортировка с поддержкой key."""
    if not a:
        return []  # пустой массив

    n = len(a)  # длина массива
    if buckets is None:
        buckets = n or 1  # по умолчанию число корзин = длине массива

    keys = [key(x) if key else x for x in a]  # получаем ключи
    min_val = min(keys)  # минимум
    max_val = max(keys)  # максимум

    bucket_list: list[list[T]] = [[] for _ in range(buckets)]  # список корзин

    for i, num in enumerate(a):
        k = keys[i]
        if max_val == min_val:
            index = 0  # все элементы одинаковы
        else:
            index = int((k - min_val) / (max_val - min_val) * (buckets - 1))  # определяем корзину
        bucket_list[index].append(num)

    def insertion_sort(bucket: list[T]) -> None:
        """Сортировка вставками для корзины."""
        for i in range(1, len(bucket)):
            key_value = bucket[i]
            key_k = key(key_value) if key else key_value  # ключ текущего элемента
            j = i - 1
            while j >= 0:
                prev_k = key(bucket[j]) if key else bucket[j]  # ключ предыдущего
                if prev_k <= key_k:
                    break
                bucket[j + 1] = bucket[j]  # сдвигаем элемент
                j -= 1
            bucket[j + 1] = key_value  # вставляем на место

    for bucket in bucket_list:
        insertion_sort(bucket)  # сортируем каждую корзину

    result: list[T] = []
    for bucket in bucket_list:
        result.extend(bucket)  # собираем результат

    a[:] = result
    return a


def heap_sort(a: list[T],
              key: Optional[Callable[[T], Any]] = None,
              cmp: Optional[Callable[[Any, Any], int]] = None) -> list[T]:
    """Пирамидальная сортировка с поддержкой key и cmp."""
    def compare(i: int, j: int) -> bool:
        """Сравнивает элементы по индексам."""
        key_i = key(a[i]) if key else a[i]  # ключ первого
        key_j = key(a[j]) if key else a[j]  # ключ второго
        if cmp:
            return cmp(key_i, key_j) > 0  # используем компаратор
        return key_i > key_j  # стандартное сравнение

    def heapify(n: int, i: int) -> None:
        """Просеивание элемента вниз."""
        largest = i  # индекс наибольшего элемента
        left = 2 * i + 1  # левый потомок
        right = 2 * i + 2  # правый потомок

        if left < n and compare(left, largest):
            largest = left  # если левый больше
        if right < n and compare(right, largest):
            largest = right  # если правый больше
        if largest != i:
            a[i], a[largest] = a[largest], a[i]  # меняем местами
            heapify(n, largest)  # рекурсивно просеиваем вниз

    n = len(a)
    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)  # строим кучу
    for i in range(n - 1, 0, -1):
        a[0], a[i] = a[i], a[0]  # переносим максимум в конец
        heapify(i, 0)  # восстанавливаем кучу
    return a


def shell_sort(a: list[T],
               key: Optional[Callable[[T], Any]] = None,
               cmp: Optional[Callable[[Any, Any], int]] = None) -> list[T]:
    """Сортировка Шелла с поддержкой key и cmp."""
    n = len(a)  # длина массива
    gap = n // 2  # начальный шаг

    def compare(x, y):
        """Сравнивает два элемента."""
        key_x = key(x) if key else x  # ключ первого
        key_y = key(y) if key else y  # ключ второго
        if cmp:
            return cmp(key_x, key_y) > 0  # используем компаратор
        return key_x > key_y  # стандартное сравнение

    while gap > 0:
        for i in range(gap, n):
            temp = a[i]  # текущий элемент
            j = i
            while j >= gap and compare(a[j - gap], temp):
                a[j] = a[j - gap]  # сдвигаем элемент вперёд
                j -= gap
            a[j] = temp  # вставляем на место
        gap //= 2  # уменьшаем шаг

    return a
