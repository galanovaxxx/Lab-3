import time


def timeit_once(func: callable, *args, **kwargs) -> float:
    """Время выполнения одной функции (секунды)."""
    start = time.perf_counter()  # стартовое время
    func(*args, **kwargs)        # вызов функции
    end = time.perf_counter()    # конечное время
    return end - start           # разница — время работы


def benchmark_sorts(arrays: dict[str, list], algos: dict[str, callable]) -> dict[str, dict[str, float]]:
    """Сравнивает алгоритмы сортировки на разных массивах."""
    results = {}  # результаты: {тип данных: {алгоритм: время}}
    for data_name, original_array in arrays.items():
        results[data_name] = {}
        for algo_name, sort_func in algos.items():
            # Копируем массив, чтобы не испортить исходный
            test_array = original_array.copy()
            # Засекаем время сортировки
            elapsed = timeit_once(sort_func, test_array)
            results[data_name][algo_name] = elapsed
            # Печатаем результат для пользователя
            print(f"{data_name:15} | {algo_name:15} | {elapsed:.6f} сек")
    return results


def print_benchmark_table(results: dict[str, dict[str, float]]):
    """Печать результатов в виде таблицы."""
    data_types = list(results.keys())  # типы данных (столбцы)
    algos = list(results[data_types[0]].keys())  # алгоритмы (строки)
    # Формируем и печатаем заголовок
    header = "Алгоритм".ljust(15) + " | " + " | ".join(dt.ljust(10) for dt in data_types)
    print(header)
    print("-" * len(header))
    # Печатаем строки с результатами
    for algo in algos:
        row = algo.ljust(15) + " | "
        times = [f"{results[dt][algo]:.6f}".ljust(10) for dt in data_types]
        row += " | ".join(times)
        print(row)