#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import sys

if __name__ == '__main__':
    x = int(input("Введите натуральное число: "))
    if x <= 0:
        print("Ошибка", file=sys.stderr)
        exit(1)
    for i in range(1,x+1):
        if x % i == 0:
            print(i)