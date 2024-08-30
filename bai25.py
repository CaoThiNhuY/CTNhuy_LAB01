# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 20:34:29 2024

@author: ny
"""

kt=input("Nhap ky tu:")
if kt.islower() and len(kt)==1:
    print("",kt.upper())
else:
    print("Khong xac dinh. Vui long nhap 1 ki tu chu thuong.")