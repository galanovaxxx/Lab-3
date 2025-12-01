def fibo(n: int) -> int:
    """Итеративное число Фибоначчи."""
    if not isinstance(n, int):
        raise ValueError("число Фибоначчи определено только для целых n")
    if n < 0:
        raise ValueError("для отрицательного n число Фибоначчи не определено")
    a, b = 0, 1  # начальные значения
    for _ in range(n):
        a, b = b, a + b  # сдвигаем пару
    return a  # результат


def fibo_recursive(n: int) -> int:
    """Рекурсивное число Фибоначчи."""
    if not isinstance(n, int):
        raise ValueError("число Фибоначчи определено только для целых n")
    if n < 0:
        raise ValueError("для отрицательного n число Фибоначчи не определено")
    if n < 2:
        return n  # базовый случай
    return fibo_recursive(n - 1) + fibo_recursive(n - 2)  # рекурсия


def factorial(n: int) -> int:
    """Итеративный факториал."""
    if not isinstance(n, int):
        raise ValueError("факториал определён только для целых чисел")
    if n < 0:
        raise ValueError("для отрицательного числа нельзя найти факториал")
    result = 1  # начальное значение
    for i in range(2, n + 1):
        result *= i  # умножаем на i
    return result  # итог


def factorial_recursive(n: int) -> int:
    """Рекурсивный факториал."""
    if not isinstance(n, int):
        raise ValueError("факториал определён только для целых чисел")
    if n < 0:
        raise ValueError("для отрицательного числа нельзя найти факториал")
    if n <= 1:
        return 1  # базовый случай
    return n * factorial_recursive(n - 1)  # рекурсия
