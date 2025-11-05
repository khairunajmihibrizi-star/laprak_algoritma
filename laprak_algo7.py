# -*- coding: utf-8 -*-
"""
Created on Wed Nov  5 21:58:28 2025

@author: khairunnajmi hibrizi
"""

def cek_prima(angka):
    if angka <=1:
        return False
    for i in range(2,int(angka**0.5)+1):
        if angka% i == 0:
            return False
    return True

def hasil(angka):
    if cek_prima(angka):
        print(f'\n{angka} bilangan prima :)')
    else:
        print(f'\n{angka} bukan bilangan prima :(')
        
bilangan=int(input('masukan angka :'))
hasil(bilangan)