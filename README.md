# practice-information-security

Учебные кейс-задачи по учебной практике (ознакомительной практике), направление 10.03.01 «Информационная безопасность», профиль «Белый хакер».

## Состав

- `case3_array` — сумма отрицательных элементов между максимумом и минимумом (Python, 10 тестов).
- `case4_dragons` — максимальная сила драконьей стаи: динамическое программирование и жадный алгоритм (Python, 6 тестов).

## Запуск

```bash
cd case3_array
python main.py

cd ../case4_dragons
python main.py
```

## Тесты

```bash
cd case3_array
python -m unittest discover -s tests -t . -v

cd ../case4_dragons
python -m unittest discover -s tests -t . -v
```

Подробные описания, примеры ввода-вывода и результаты тестирования находятся в `README.md` внутри каждой папки.
