# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 19:29:34 2024

@author: ny
"""
# bài 26a
a = int(input("Nhap so a: "))
b = int(input("Nhap so b: "))
c = int(input("Nhap so c: "))
if a > b:
    a,b=b,a
if a > c:
    a,c=c,a
if b > c:
    b,c=c,b
print("Thu tu tang dan la: ",a, b, c)
#bài 26b
a = int(input("Nhap so a: "))
b = int(input("Nhap so b: "))
c = int(input("Nhap so c: "))
d = int(input("Nhap so d: "))
if a > b:
    a,b=b,a
if a > c:
    a,c=c,a
if a > d:
    a,d=d,a
if b > c:
    b,c=c,b
if b > d:
    b,d=d,b
if c > d:
    c,d=d,c
print("Cac con so theo thu tu tang dan.",a,b,c,d)