# -*- coding: utf-8 -*-
"""
Created on Tue Nov 11 22:00:40 2025

@author: khairunnajmi hibrizi
"""

def ordinal():
    print('ordinal number')
    
    def akhiran(i):
        if 10 <= i % 100 <= 20:
            return 'th'
        else:
            if i % 10 ==1:
                return 'st'
            elif i % 10 ==2:
                return 'nd'
            elif i % 10 ==3:
                return 'rd'
            else:
                return 'th'
    
    while True:
        angka=int(input('masukan angka(0 untuk berhenti):'))
        if angka==0:
            print('sudah selesai :D')
            break
        else:
            print(angka,akhiran(angka))
ordinal()
        