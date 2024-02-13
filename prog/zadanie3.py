#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def multiply_until_zero():
    product = 1
    while True:
        num = int(input("Введите число (для завершения введите 0): "))
        if num == 0:
            break
        product *= num
    return product

if __name__ == "__main__":
    result = multiply_until_zero()
    print("Результат умножения:", result)
