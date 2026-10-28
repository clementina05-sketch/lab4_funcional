"""
Задание 8 (повышенная сложность): Фильтрация и преобразование CSV
через map/filter.
"""
import csv


def create_test_csv(filename):
    """Создает тестовый CSV-файл для демонстрации."""
    data = [
        ["Имя", "Возраст", "Город"],
        ["Анна", "25", "Москва"],
        ["Иван", "17", "Санкт-Петербург"],
        ["Мария", "30", "Казань"],
        ["Петр", "15", "Новосибирск"],
        ["Ольга", "22", "Москва"]
    ]
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)


def process_csv(filename):
    """Читает CSV, фильтрует совершеннолетних и преобразует возраст."""
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)  # Пропускаем заголовок
        rows = list(reader)

    # 1. Фильтрация: оставляем только тех, кому 18 и больше
    adults = list(filter(lambda row: int(row[1]) >= 18, rows))

    # 2. Преобразование: создаем список строк "Имя (Город) - Возраст лет"
    formatted_adults = list(
        map(lambda row: f"{row[0]} ({row[2]}) - {row[1]} лет", adults)
    )

    return header, formatted_adults


if __name__ == "__main__":
    csv_filename = "data.csv"
    create_test_csv(csv_filename)

    header, result = process_csv(csv_filename)

    print(f"Заголовок: {header}")
    print("Совершеннолетние пользователи:")
    for line in result:
        print(f"- {line}")