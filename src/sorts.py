import random


def bubble_sort(a: list[int]) -> list[int]:
    """
    Сортировка пузырьком (bubble sort).
    Меняет элементы местами, пока не будет отсортировано по возрастанию.
    """
    n = len(a)  # длина массива
    for i in range(n):  # внешний цикл по всем элементам
        swapped = False  # флаг для оптимизации
        for j in range(n - i - 1):  # внутренний цикл до неотсортированной части
            if a[j] > a[j + 1]:  # если текущий больше следующего
                a[j], a[j + 1] = a[j + 1], a[j]  # меняем местами
                swapped = True  # был обмен
        if not swapped:  # если не было обменов — массив уже отсортирован
            break
    return a  # возвращаем отсортированный массив (тот же объект)


def quick_sort(a: list[int]) -> list[int]:
    """
    Быстрая сортировка (quick sort).
    Рекурсивно делит массив на три части относительно опорного элемента (pivot).
    """
    if len(a) <= 1:
        return a  # базовый случай: массив из 0 или 1 элемента уже отсортирован

    pivot = random.choice(a)  # выбираем случайный опорный элемент
    lower = [x for x in a if x < pivot]  # элементы меньше опорного
    equal = [x for x in a if x == pivot]  # равные опорному
    higher = [x for x in a if x > pivot]  # больше опорного

    sorted_result = quick_sort(lower) + equal + quick_sort(higher)  # рекурсивно сортируем части
    a[:] = sorted_result  # копируем результат обратно в исходный массив
    return a


def counting_sort(a: list[int]) -> list[int]:
    """
    Сортировка подсчётом (counting sort).
    Работает только с целыми числами, поддерживает отрицательные.
    """
    if not a:
        return []  # пустой массив

    min_val = min(a)  # минимальное значение
    max_val = max(a)  # максимальное значение
    range_size = max_val - min_val + 1  # диапазон значений

    count = [0] * range_size  # массив для подсчёта количества каждого значения
    output = [0] * len(a)  # выходной массив

    for num in a:
        count[num - min_val] += 1  # увеличиваем счётчик для каждого числа

    for i in range(1, len(count)):
        count[i] += count[i - 1]  # делаем массив накопительным

    for num in reversed(a):  # идём с конца для устойчивости
        idx = num - min_val
        count[idx] -= 1
        output[count[idx]] = num

    a[:] = output  # копируем результат обратно
    return a


def radix_sort(a: list[int], base: int = 10) -> list[int]:
    """
    Поразрядная сортировка (radix sort, LSD).
    Работает с целыми числами, поддерживает отрицательные.
    """
    def _radix_non_negative(nums: list[int]) -> list[int]:
        if not nums:
            return []  # пустой список

        exp = 1  # текущий разряд
        max_val = max(nums)  # максимальное значение
        result = list(nums)  # копия

        while max_val // exp > 0:
            buckets = [[] for _ in range(base)]  # корзины для каждого значения разряда
            for num in result:
                digit = (num // exp) % base  # выделяем цифру
                buckets[digit].append(num)

            result = [num for bucket in buckets for num in bucket]  # собираем обратно
            exp *= base  # переходим к следующему разряду

        return result

    if not a:
        return []

    positives = [num for num in a if num >= 0]  # положительные числа
    negatives = [-num for num in a if num < 0]  # отрицательные (по модулю)

    sorted_pos = _radix_non_negative(positives)  # сортируем положительные
    sorted_neg = _radix_non_negative(negatives)  # сортируем отрицательные

    result = [-num for num in reversed(sorted_neg)] + sorted_pos  # собираем итог
    a[:] = result
    return a


def bucket_sort(a: list[float], buckets: int | None = None) -> list[float]:
    """
    Блочная сортировка (bucket sort).
    Делит массив на корзины по диапазону значений, сортирует каждую корзину вставками.
    """
    if not a:
        return []  # пустой массив

    n = len(a)  # длина массива
    if buckets is None:
        buckets = n or 1  # по умолчанию число корзин = длине массива

    min_val = min(a)  # минимум
    max_val = max(a)  # максимум

    bucket_list: list[list[float]] = [[] for _ in range(buckets)]  # список корзин

    for num in a:
        if max_val == min_val:
            index = 0  # все элементы одинаковы
        else:
            index = int((num - min_val) / (max_val - min_val) * (buckets - 1))  # определяем корзину
        bucket_list[index].append(num)

    def insertion_sort(bucket: list[float]) -> None:
        for i in range(1, len(bucket)):
            key_value = bucket[i]
            j = i - 1
            while j >= 0 and bucket[j] > key_value:
                bucket[j + 1] = bucket[j]
                j -= 1
            bucket[j + 1] = key_value

    for bucket in bucket_list:
        insertion_sort(bucket)  # сортируем каждую корзину

    result: list[float] = []
    for bucket in bucket_list:
        result.extend(bucket)  # собираем результат

    a[:] = result
    return a


def heap_sort(a: list[int]) -> list[int]:
    """
    Пирамидальная сортировка (heap sort).
    Строит max-heap и поочерёдно извлекает максимумы.
    """
    def heapify(arr: list[int], n: int, i: int) -> None:
        largest = i  # индекс наибольшего элемента
        left = 2 * i + 1  # левый потомок
        right = 2 * i + 2  # правый потомок

        if left < n and arr[left] > arr[largest]:
            largest = left  # если левый больше
        if right < n and arr[right] > arr[largest]:
            largest = right  # если правый больше
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # меняем местами
            heapify(arr, n, largest)  # рекурсивно просеиваем вниз

    n = len(a)
    for i in range(n // 2 - 1, -1, -1):
        heapify(a, n, i)  # строим кучу
    for i in range(n - 1, 0, -1):
        a[0], a[i] = a[i], a[0]  # переносим максимум в конец
        heapify(a, i, 0)  # восстанавливаем кучу
    return a


def shell_sort(a: list[int]) -> list[int]:
    """
    Сортировка Шелла (shell sort).
    Использует последовательность шагов gap, постепенно уменьшая её.
    """
    n = len(a)  # длина массива
    gap = n // 2  # начальный шаг

    while gap > 0:
        for i in range(gap, n):
            temp = a[i]  # текущий элемент
            j = i
            while j >= gap and a[j - gap] > temp:
                a[j] = a[j - gap]  # сдвигаем элемент вперёд
                j -= gap
            a[j] = temp  # вставляем на место
        gap //= 2  # уменьшаем шаг

    return a