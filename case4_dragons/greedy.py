#!/usr/bin/env python3
"""Жадный алгоритм для задачи о максимальной силе драконьей стаи.

Оптимальное разбиение состоит из троек; остаток 0 покрывается тройками,
остаток 1 заменяется на 2 + 2 (или 4), остаток 2 добавляется двойкой.
Такой алгоритм работает за O(log N) при возведении в степень и требует
O(1) дополнительной памяти, если не нужно выводить само разбиение.
"""


def greedy_strength(heads):
    """Возвращает максимальную силу и разбиение, построенное жадно."""
    if not 0 < heads < 100:
        raise ValueError("N должно быть целым числом от 1 до 99")

    if heads == 1:
        parts = [1]
    elif heads == 2:
        parts = [2]
    elif heads == 3:
        parts = [3]
    elif heads == 4:
        parts = [4]
    elif heads % 3 == 0:
        parts = [3] * (heads // 3)
    elif heads % 3 == 1:
        # 3 + 1 хуже, чем 2 + 2, поэтому четвёрку добавляем отдельно.
        parts = [3] * ((heads - 4) // 3) + [4]
    else:
        parts = [3] * ((heads - 2) // 3) + [2]

    parts.sort(reverse=True)

    strength = 1
    for part in parts:
        strength *= part

    return strength, parts


def main():
    print("Максимальная сила драконьей стаи (жадный алгоритм)")
    try:
        heads = int(input("Введите количество голов N (1..99): ").strip())
    except ValueError:
        print("Ошибка: введите целое число.")
        return

    try:
        strength, parts = greedy_strength(heads)
    except ValueError as error:
        print("Ошибка:", error)
        return

    print(f"\nКоличество голов: {heads}")
    print(f"Максимальная сила стаи: {strength}")
    print(f"Количество драконов: {len(parts)}")
    print("Оптимальное разбиение:", " + ".join(map(str, parts)), "=", sum(parts))
    print("Проверка произведения:", " * ".join(map(str, parts)), "=", strength)


if __name__ == "__main__":
    main()
