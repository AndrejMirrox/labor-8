#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    s = input("Введите строку: ")
    i = 0
    while i < len(s):
        if s[i].lower() == "и" and i % 2 == 0:
            print(f"{s[i]}  => [{i}]")
        i += 1