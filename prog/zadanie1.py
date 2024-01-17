#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def positive():
    print("Положительное")

def negative():
    print("Отрицательное")

def test():
    number = int(input("Введите целое число: "))
    if number > 0:
        positive()
    elif number < 0:
        negative()

if __name__ == '__main__':
    test()
