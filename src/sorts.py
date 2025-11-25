import random


def bubble_sort(a: list[int]) -> list[int]:
    n = len(a)
    for i in range(n):
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


def quick_sort(a: list[int]) -> list[int]:
    n = len(a)
    if n <= 1:
        return a
    else:
        pivot = random.choice(a)
        less = [x for x in a if x < pivot]
        greater_or_equal = [x for x in a if x >= pivot]
        return quick_sort(less) + quick_sort(greater_or_equal)


def counting_sort(a: list[int]) -> list[int]:
    max_val = max(a)
    count = [0] * (max_val + 1)
    output = [0] * len(a)
    for num in a:
        count[num] += 1
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    for num in reversed(a):
        output[count[num] - 1] = num
        count[num] -= 1
    for i in range(len(a)):
        a[i] = output[i]
    return a


def radix_sort(a: list[int], base: int = 10) -> list[int]:
    if not a:
        return a
    max_val = max(a)
    exp = 1
    while max_val // exp > 0:
        buckets = [[] for _ in range(base)]
        for num in a:
            digit = (num // exp) % base
            buckets[digit].append(num)
        a = []
        for bucket in buckets:
            a.extend(bucket)
        exp *= base
    return a


def bucket_sort(a: list[float], buckets: int | None = None) -> list[float]:
    if not a:
        return a
    n = len(a)
    if buckets is None:
        buckets = n
    min_val = min(a)
    max_val = max(a)
    bucket_list = [[] for _ in range(buckets)]
    for num in a:
        if max_val == min_val:
            index = 0
        else:
            index = int((num - min_val) / (max_val - min_val) * (buckets - 1))
        bucket_list[index].append(num)
    for i in range(buckets):
        bucket_list[i].sort()
    result = []
    for bucket in bucket_list:
        result.extend(bucket)
    return result


def heap_sort(a: list[int]) -> list[int]:
    def heapify(arr: list[int], n: int, i: int) -> list[int]:
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)
    n = len(a)
    for i in range(n // 2 - 1, -1, -1):
        heapify(a, n, i)
    for i in range(n - 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        heapify(a, i, 0)
    return a