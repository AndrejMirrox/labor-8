#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

if __name__ == '__main__':
    x = int(input("Сколько кг было соьрано за день? : "))
    if x < 0:
        print("Ошиблчка!", file=sys.stderr)
        exit(1)
    if x < 50:
        s = x * 30
        print(f"Заработал за день: {s//100} руб. {s%100} коп.")
    elif x >= 50 and x < 75:
        s = x * 50
        print(f"Заработал за день: {s // 100} руб. {s % 100} коп.")
    elif x >= 75 and x < 90:
        s = x * 65
        print(f"Заработал за день: {s // 100} руб. {s % 100} коп.")
    else:
        s = x * 70
        print(f"Заработал за день: {s // 100 + 20} руб. {s % 100} коп.")
