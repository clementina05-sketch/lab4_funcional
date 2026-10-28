"""
Задание 1 (средняя сложность): Вычислить квадраты чисел 1–10 с map.
"""


if __name__ == "__main__":
    numbers = list(range(1, 11))

    # Использование map с lambda-функцией
    squares = list(map(lambda x: x ** 2, numbers))

    print(f"Исходные числа: {numbers}")
    print(f"Квадраты чисел: {squares}")