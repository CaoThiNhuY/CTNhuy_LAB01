# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 22:06:05 2024

@author: Admin
"""

hh=int(input("Nhap gio:"))
mm=int(input("Nhap phut:"))
ss=int(input("Nhap giay:"))
print("Theo dinh dang: {}:{}:{}".format(hh,mm,ss))
tong_giay=hh*60*60 +mm*60 + ss
print("Tong giay la:", tong_giay)