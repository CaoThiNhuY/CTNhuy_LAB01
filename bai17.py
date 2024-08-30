# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 22:15:00 2024

@author: Admin
"""

a = int(input("Nhap so nguyen thu nhat: "))
b = int(input("Nhap so nguyen thu hai: "))
c = int(input("Nhap so nguyen thu ba: "))
max_so = max(a, b, c)
min_so = min(a, b, c)
print("So lon nhat là:", max_so)
print("So nho nhat là:", min_so)