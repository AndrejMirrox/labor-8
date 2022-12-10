#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    s = input("Введите строку: ")
    i = 0
    while i < len(s):
        if s[i].lower() == "н" or s[i].lower() == "к":
            print(f"Первая буква: {s[i]} => [{i}]")
            break
        i += 1