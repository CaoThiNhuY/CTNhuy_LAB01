# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 14:10:05 2024

@author: Admin
"""
import math
h=int(input("Nhap gio (1):"))
p=int(input("Nhap phut (1):"))
s=int(input("Nhap giay (1):"))
t1=h*3600+p*60+s
print("t1=",t1)
h2=int(input("Nhap gio (2):"))
p2=int(input("Nhap phut (2):"))
s2=int(input("Nhap giay (2):"))
t2=h2*3600+p2*60+s2
print("t2=",t2)
print("Tong 2 gio la:",t1+t2)
print("Hieu 2 gio la:",t1-t2)