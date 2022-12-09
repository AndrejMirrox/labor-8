#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import sys


if __name__ == '__main__':
    x = int(input("Введите первое натуральное число: "))
    y = int(input("Введите второе натуральное число: "))
    if x < 0 or y <= 0:
        print("Одно или оба числа меньше нуля", file=sys.stderr)
        exit(1)
    if x % y == 0:
        print(f"Числа делятся без остатка, результат деления: {x / y}")
    else:
        print(f"Числа не делятся нацело, остаток от деления: {x % y}")
