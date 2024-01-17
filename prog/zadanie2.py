#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def cylinder():
    radius = float(input("Введите радиус цилиндра: "))
    height = float(input("Введите высоту цилиндра: "))
    
    def circle():
        return math.pi * radius ** 2
    
    choice = input("Введите '1' для расчета площади боковой поверхности, или '2' для расчета полной площади цилиндра: ")
    
    if choice == '1':
        lateral_area = 2 * math.pi * radius * height
        print("Площадь боковой поверхности цилиндра:", lateral_area)
    elif choice == '2':
        lateral_area = 2 * math.pi * radius * height
        total_area = lateral_area + 2 * circle()
        print("Полная площадь цилиндра:", total_area)
    else:
        print("Некорректный выбор.")

cylinder()