#!/usr/bin/env python3
"""Сумма отрицательных элементов между максимумом и минимумом.

Программа запрашивает размер массива N и N целых чисел, находит первое
вхождение максимального и первого вхождения минимального элемента, после
чего суммирует отрицательные элементы, расположенные строго между ними.
"""


def find_first_extremes(values):
    """Возвращает индексы первых вхождений максимума и минимума."""
    if not values:
        raise ValueError("Массив не должен быть пустым")

    max_index = 0
    min_index = 0

    for i in range(1, len(values)):
        if values[i] > values[max_index]:
            max_index = i
        if values[i] < values[min_index]:
            min_index = i

    return max_index, min_index


def sum_negatives_between(values):
    """Суммирует отрицательные элементы строго между максимумом и минимумом.

    Возвращает кортеж: (сумма, индекс максимума, индекс минимума,
    левая граница, правая граница).
    """
    max_index, min_index = find_first_extremes(values)
    left = min(max_index, min_index)
    right = max(max_index, min_index)

    total = sum(
        value for value in values[left + 1:right]
        if value < 0
    )

    return total, max_index, min_index, left, right


def read_int(prompt):
    """Читает целое число с повторным запросом при ошибке."""
    while True:
        raw = input(prompt).strip()
        try:
            return int(raw)
        except ValueError:
            print("Ошибка: введите целое число.")


def read_array(size):
    """Читает ровно size целых чисел, допуская ввод в несколько строк."""
    values = []
    print(f"Введите {size} целых чисел (можно в одной строке через пробел или по одному):")

    while len(values) < size:
        parts = input().split()
        if not parts:
            continue

        for part in parts:
            try:
                values.append(int(part))
            except ValueError:
                print(f"Значение «{part}» не является целым числом и пропущено.")
            if len(values) == size:
                break

    return values


def main():
    print("Поиск суммы отрицательных элементов между максимумом и минимумом")
    size = read_int("Введите количество элементов N: ")

    if size <= 0:
        print("Ошибка: N должно быть положительным.")
        return

    values = read_array(size)
    total, max_index, min_index, left, right = sum_negatives_between(values)

    between = values[left + 1:right]

    print("\nИсходный массив:", values)
    print(f"Максимум: a[{max_index}] = {values[max_index]}")
    print(f"Минимум:  a[{min_index}] = {values[min_index]}")
    print("Элементы между ними:", between if between else "нет")
    print("Сумма отрицательных элементов:", total)


if __name__ == "__main__":
    main()
