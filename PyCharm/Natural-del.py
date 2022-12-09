#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import sys


if __name__ == '__main__':
    x = int(input("Введите натуральное число: "))
    i = 1
    if x <= 0:
        print("Ошибка", file=sys.stderr)
        exit(1)
    while i <= x:
        if x % i == 0:
            print(i)
        i += 1