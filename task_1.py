"""
Задание 5 (средняя сложность): Создать генератор Фибоначчи.
"""


def fibonacci_generator(n):
    """Генератор, возвращающий n чисел Фибоначчи."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    print("Первые 10 чисел Фибоначчи:")
    for num in fibonacci_generator(10):
        print(num, end=" ")
    print()