#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    # Ввести список одной строкой
    a = list(map(int, input().split()))
    # Если список пуст, завершить программу
    if len(a) != 10:
        print("Заданный список не тот", file=sys.stderr)
        exit(1)
    # Определить индексы минимального и максимального элемента
    count = 0
    s = sum([num for ind, num in enumerate(a) if abs(num) < 3])
    count = len([num for ind, num in enumerate(a) if num % 9 == 0])
    print(f"Количество: {count}\nСумма: {s}")