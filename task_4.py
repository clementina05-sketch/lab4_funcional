"""
Задание 6 (повышенная сложность): Создать декоратор с параметрами.
"""


def repeat(times):
    """Декоратор, который повторяет вызов функции заданное количество раз."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Выполнение функции {func.__name__} {times} раз(а):")
            result = None
            for i in range(times):
                result = func(*args, **kwargs)
                print(f"  Попытка {i + 1}: {result}")
            return result
        return wrapper
    return decorator


@repeat(times=3)
def greet(name):
    """Приветствует пользователя."""
    return f"Привет, {name}!"


if __name__ == "__main__":
    greet("Мир")