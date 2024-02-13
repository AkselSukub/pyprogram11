#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_input():
    return input("Введите значение: ")

def test_input(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def str_to_int(value):
    return int(value)

def print_int(value):
    print(value)

# Основная программа
if __name__ == "__main__":
    input_value = get_input()

if test_input(input_value):
    integer_value = str_to_int(input_value)
    print_int(integer_value)
else:
    print("Невозможно преобразовать в целое число.")
