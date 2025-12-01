from sys import stdin

from src.factorial_fibo import factorial, factorial_recursive, fibo, fibo_recursive
from src.sorting_utils import (
    bubble_sort,
    quick_sort,
    counting_sort,
    radix_sort,
    bucket_sort,
    heap_sort,
    shell_sort,
)
from src.stack import Stack
from src.queue import Queue


def main():
    print(
        'Команды:\n'
        '  fact <n>                    - факториал итеративный\n'
        '  fact_r <n>                  - факториал рекурсивный\n'
        '  fibo <n>                    - фибоначчи итеративный\n'
        '  fibo_r <n>                  - фибоначчи рекурсивный\n'
        '  bubble <числа>              - сортировка пузырьком\n'
        '  quick <числа>               - быстрая сортировка\n'
        '  counting <числа>            - сортировка подсчётом\n'
        '  radix <числа>               - поразрядная сортировка\n'
        '  bucket <числа>              - блочная сортировка\n'
        '  heap <числа>                - пирамидальная сортировка\n'
        '  shell <числа>               - сортировка Шелла\n'
        '  bubble_key len <слова>      - сортировка по ключу (len)\n'
        '  quick_key neg <числа>       - сортировка по ключу (neg = по убыванию)\n'
        '  bubble_cmp <числа>          - сортировка с компаратором (по убыванию)\n'
        '  stack push/pop/min/show <n> - работа со стеком\n'
        '  queue enq/deq/show <val>    - работа с очередью\n'
        '  exit                        - выход\n'
    )

    stack = Stack()
    queue = Queue()

    for line in stdin:
        try:
            parts = line.strip().split()
            if not parts:
                continue

            cmd = parts[0].lower()
            args = parts[1:]

            # выход
            if cmd in ['exit', 'quit', 'стоп']:
                break

            # факториал
            elif cmd == 'fact':
                n = int(args[0])
                print(factorial(n))

            elif cmd == 'fact_r':
                n = int(args[0])
                print(factorial_recursive(n))

            # фибоначчи
            elif cmd == 'fibo':
                n = int(args[0])
                print(fibo(n))

            elif cmd == 'fibo_r':
                n = int(args[0])
                print(fibo_recursive(n))

            # сортировки (целые числа)
            elif cmd == 'bubble':
                data = [int(x) for x in args]
                print(bubble_sort(data))

            elif cmd == 'quick':
                data = [int(x) for x in args]
                print(quick_sort(data))

            elif cmd == 'counting':
                data = [int(x) for x in args]
                print(counting_sort(data))

            elif cmd == 'radix':
                data = [int(x) for x in args]
                print(radix_sort(data))

            elif cmd == 'heap':
                data = [int(x) for x in args]
                print(heap_sort(data))

            elif cmd == 'shell':
                data = [int(x) for x in args]
                print(shell_sort(data))

            elif cmd == 'bucket':
                data = [float(x) for x in args]
                print(bucket_sort(data))

            # сортировки с ключом
            elif cmd == 'bubble_key':
                key_name = args[0]
                values = args[1:]
                if key_name == 'len':
                    print(bubble_sort(values, key=len))
                elif key_name == 'neg':
                    data = [int(x) for x in values]
                    print(bubble_sort(data, key=lambda x: -x))

            elif cmd == 'quick_key':
                key_name = args[0]
                values = args[1:]
                if key_name == 'len':
                    print(quick_sort(values, key=len))
                elif key_name == 'neg':
                    data = [int(x) for x in values]
                    print(quick_sort(data, key=lambda x: -x))

            elif cmd == 'heap_key':
                key_name = args[0]
                values = args[1:]
                if key_name == 'len':
                    print(heap_sort(values, key=len))
                elif key_name == 'neg':
                    data = [int(x) for x in values]
                    print(heap_sort(data, key=lambda x: -x))

            elif cmd == 'shell_key':
                key_name = args[0]
                values = args[1:]
                if key_name == 'len':
                    print(shell_sort(values, key=len))
                elif key_name == 'neg':
                    data = [int(x) for x in values]
                    print(shell_sort(data, key=lambda x: -x))

            # сортировки с компаратором (по убыванию)
            elif cmd == 'bubble_cmp':
                data = [int(x) for x in args]
                cmp_desc = lambda a, b: -1 if a > b else (1 if a < b else 0)
                print(bubble_sort(data, cmp=cmp_desc))

            elif cmd == 'quick_cmp':
                data = [int(x) for x in args]
                cmp_desc = lambda a, b: -1 if a > b else (1 if a < b else 0)
                print(quick_sort(data, cmp=cmp_desc))

            elif cmd == 'heap_cmp':
                data = [int(x) for x in args]
                cmp_desc = lambda a, b: -1 if a > b else (1 if a < b else 0)
                print(heap_sort(data, cmp=cmp_desc))

            elif cmd == 'shell_cmp':
                data = [int(x) for x in args]
                cmp_desc = lambda a, b: -1 if a > b else (1 if a < b else 0)
                print(shell_sort(data, cmp=cmp_desc))

            # стек
            elif cmd == 'stack':
                action = args[0] if args else 'show'
                if action == 'push':
                    stack.push(int(args[1]))
                    print(f'pushed {args[1]}')
                elif action == 'pop':
                    print(stack.pop())
                elif action == 'min':
                    print(stack.min())
                elif action == 'top':
                    print(stack.top())
                elif action == 'show':
                    print(stack.items)

            # очередь
            elif cmd == 'queue':
                action = args[0] if args else 'show'
                if action == 'enq':
                    queue.enqueue(args[1])
                    print(f'enqueued {args[1]}')
                elif action == 'deq':
                    print(queue.dequeue())
                elif action == 'front':
                    print(queue.front())
                elif action == 'show':
                    print(queue.items)

            else:
                print('неизвестная команда')

        except IndexError:
            print('недостаточно аргументов')
        except ValueError as e:
            print(f'ошибка: {e}')
        except Exception as e:
            print(f'ошибка: {e}')


if __name__ == '__main__':
    main()
