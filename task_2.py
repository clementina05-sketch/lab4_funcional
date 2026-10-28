"""
Задание 7 (средняя сложность): Написать декоратор для логирования
вызова функции.
"""


def log_calls(func):
    """Декоратор, который логирует вызов функции и её аргументы."""
    def wrapper(*args, **kwargs):
        print(f"Вызов функции: {func.__name__}")
        print(f"Аргументы: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"Результат: {result}")
        return result
    return wrapper


@log_calls
def add(a, b):
    """Складывает два числа."""
    return a + b


if __name__ == "__main__":
    add(5, 10)