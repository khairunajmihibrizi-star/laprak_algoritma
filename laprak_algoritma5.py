# -*- coding: utf-8 -*-
"""
Created on Tue Oct 21 16:57:29 2025

@author: khairunnajmi hibrizi
"""

def tiket_tertentu(umur):
    if umur<=2:
        return 0
    elif 3<= umur <=12:
        return 14
    elif umur >= 65:
        return 18
    else:
        return 23
total_kembalian=0
pembayaran=0

while True:
    umur=int(input('masukan umur anda (-1 untuk keluar) :'))
    if umur == -1:
        break
    
    harga_tiket =tiket_tertentu(umur)
    print(f'tiket_tertentu :${harga_tiket}')
    
    if harga_tiket > 0:
        bayar= int(input('masukan uang pembayaran anda :$')) 
        
        if bayar < harga_tiket:
            print(f'uang tidak cukup, uang yang harus dibayar minimal ${harga_tiket}')
            
        else:
            kembalian= bayar-harga_tiket
            if kembalian > 0:
                print(f'kembalian:${kembalian}')
                
pembayaran +=harga_tiket
total_kembalian +=kembalian
print('\n=====+=====')
print(f'total pembayaran :${pembayaran}')
print(f'total kembalian :${kembalian}')
print('-selamat liburan-')