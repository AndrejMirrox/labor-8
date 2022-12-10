#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    wrong = "рпроцессо"

    # Берём первый символ
    part_end = wrong[:1]

    # Берём остальные сиволы
    part_start = wrong[1:]

    # Соединяем части
    print(part_start + part_end)