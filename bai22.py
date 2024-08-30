# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 18:43:43 2024

@author: ny
"""
import math
a=float(input("Nhap a="))
b=float(input("Nhap b="))
print("{0}x+{1}=0".format(a,b))
if a!=0:
    x=-b/a
    print("Phuong trinh co nghiem duy nhat: x=",x)
else:
    if b==0:
        print("Phuong trinh co vo so nghiem")
    else:
        print("Phuong trinh vo nghiem")
    
