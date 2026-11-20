#!/usr/bin/env python3
"""Максимальная сила драконьей стаи.

Каждый дракон имеет от 1 до 7 голов. Сила стаи равна произведению чисел
голов всех драконов. Требуется распределить N голов так, чтобы произведение
было максимальным.

Реализовано динамическое программирование с восстановлением разбиения.
"""


MAX_HEADS_PER_DRAGON = 7


def max_strength(heads):
    """Возвращает максимальную силу и оптимальное разбиение числа heads.

    Динамика: dp[s] — максимальное произведение для s голов.
    dp[0] = 1 (пустое произведение), dp[s] = max(dp[s-k] * k) для 1 <= k <= 7.
    Массив choice[s] хранит выбранное k, чтобы восстановить разбиение.
    """
    if not 0 < heads < 100:
        raise ValueError("N должно быть целым числом от 1 до 99")

    dp = [0] * (heads + 1)
    choice = [0] * (heads + 1)
    dp[0] = 1

    for total in range(1, heads + 1):
        best = -1
        best_k = 1
        # Перебираем k по убыванию: при равном произведении выбираем
        # большее слагаемое, чтобы разбиение было нагляднее.
        for k in range(min(MAX_HEADS_PER_DRAGON, total), 0, -1):
            candidate = dp[total - k] * k
            if candidate > best:
                best = candidate
                best_k = k
        dp[total] = best
        choice[total] = best_k

    parts = []
    remaining = heads
    while remaining > 0:
        k = choice[remaining]
        parts.append(k)
        remaining -= k
    parts.sort(reverse=True)

    return dp[heads], parts


def read_int(prompt):
    """Читает целое число с повторным запросом при ошибке."""
    while True:
        raw = input(prompt).strip()
        try:
            return int(raw)
        except ValueError:
            print("Ошибка: введите целое число.")


def main():
    print("Максимальная сила драконьей стаи")
    heads = read_int("Введите количество голов N (1..99): ")

    try:
        strength, parts = max_strength(heads)
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
