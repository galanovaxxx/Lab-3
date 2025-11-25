def fibo(n: int) -> int:
    if type(n) != int:
        raise ValueError("для вещественного числа нельзя найти число Фибоначчи")
    n1 = 0
    n2 = 1
    k = 0
    while k != n:
        n1, n2 = (n1, n2 + n1) if n2 < n1 else (n2 + n1, n2)
        k += 1
    return min(n1, n2)


def fibo_recursive(n: int) -> int:
    if type(n) != int:
        raise ValueError("для вещественного числа нельзя найти число Фибоначчи")
    if n < 2:
        return 1
    return fibo_recursive(n - 1) + fibo_recursive(n - 2)


def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("для отрицательного числа нельзя найти факториал")
    if type(n) != int:
        raise ValueError("для вещественного числа нельзя найти факториал")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def factorial_recursive(n: int) -> int:
    if n < 0:
        raise ValueError("для отрицательного числа нельзя найти факториал")
    if type(n) != int:
        raise ValueError("для вещественного числа нельзя найти факториал")
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)
