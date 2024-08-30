# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 22:23:49 2024

@author: Admin
"""

#Nhap ngay, thang, nam xuat theo dinh dang
ngay=input("Nhap ngay:")
thang=input("Nhap thang:")
nam=input("Nhap nam:")
#aa/bb/cccc
print("{}/{}/{}".format(ngay,thang,nam))
#aa/bb/cc
print("{}/{}/{}".format(ngay,thang,nam[2:]))
#cccc/bb/aa
print("{}/{}/{}".format(nam,thang,nam))