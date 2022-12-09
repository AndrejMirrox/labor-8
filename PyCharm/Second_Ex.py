#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    word = input("Введите слово: ")

    idx = len(word) // 2
    if len(word) % 2 == 1:
        # Длина слова нечётная
        r = word[:idx] + word[idx+1:]
    else:
        # Длина слова чётная
        r = word[:idx-1] + word[idx+1:]
    print(r)