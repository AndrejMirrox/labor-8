#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    # Ввести список одной строкой
    a = list(map(float, input().split()))
    # Если список пуст, завершить программу
    a_min = a[0]
    i_min = 0
    for i, item in enumerate(a):
        if item < a_min:
            i_min, a_min = i, item
    count = 0
    count = len([num for ind, num in enumerate(a) if num == 0])
    s = sum([num for ind, num in enumerate(a) if ind > i_min])

    print(f"Количество: {count}\nСумма: {s}\n")
    print(f"Остортированный массив:\n{sorted(a, key=abs)}")