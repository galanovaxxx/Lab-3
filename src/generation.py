import random


def rand_int_array(n: int, lo: int, hi: int, *, distinct: bool = False, seed = None) -> list[int]:
    """Массив случайных целых чисел."""
    if seed is not None:
        random.seed(seed)  # фиксируем зерно
    if distinct:
        if n > (hi - lo + 1):
            raise ValueError(f"Невозможно создать {n} уникальных чисел в диапазоне [{lo}, {hi}]")
        return random.sample(range(lo, hi + 1), n)  # уникальные значения
    else:
        return [random.randint(lo, hi) for _ in range(n)]  # допускаются повторы


def nearly_sorted(n: int, swaps: int, *, seed = None) -> list[int]:
    """Почти отсортированный массив."""
    if seed is not None:
        random.seed(seed)  # фиксируем зерно
    arr = list(range(1, n + 1))  # отсортированный массив
    for _ in range(swaps):
        i = random.randint(0, n - 1)  # случайный индекс
        j = random.randint(0, n - 1)
        arr[i], arr[j] = arr[j], arr[i]  # меняем местами
    return arr


def many_duplicates(n: int, k_unique: int = 5, *, seed = None) -> list[int]:
    """Массив с дубликатами."""
    if seed is not None:
        random.seed(seed)
    if k_unique > n:
        k_unique = n  # не больше n уникальных
    unique_values = list(range(1, k_unique + 1))  # список уникальных
    arr = [random.choice(unique_values) for _ in range(n)]  # наполняем дубликатами
    return arr


def reverse_sorted(n: int) -> list[int]:
    """Массив от n до 1."""
    return list(range(n, 0, -1))  # обратный порядок


def rand_float_array(n: int, lo: float = 0.0, hi: float = 10.0, *, seed = None) -> list[float]:
    """Массив случайных float."""
    if seed is not None:
        random.seed(seed)
    return [random.uniform(lo, hi) for _ in range(n)]  # случайные float