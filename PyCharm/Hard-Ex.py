#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    s = input("Введите предложение: ")
    s = s.split(" ")
    k = len(s) - 1
    i = ""
    while k >= 0:
        i += s[k] + " "
        k -= 1
    print(i)
