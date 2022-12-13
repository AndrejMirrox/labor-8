#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    k = list(map(int, input().split()))
    a = sorted(k, reverse=True)
    a = tuple(a)
    del(k)
    count = a.count(5)
    print(f"Кол-во уч. с 5: {count}\n")
    print(f"Отсортированный кортеж: {a}")
