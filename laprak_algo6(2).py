# -*- coding: utf-8 -*-
"""
Created on Tue Nov  4 19:36:44 2025

@author: khairunnajmi hibrizi
"""

def cek_kabisat(tahun):
    if tahun%400 == 0 or tahun%4 == 0 and tahun%100 != 0:
        return True
    else:
        return False
def jumlah_hari(bulan, tahun):
    
    kabisat= cek_kabisat(tahun)
    
    if bulan==1:
        nama_bulan='januari'
        hari= 31
    elif bulan== 2:
        nama_bulan= 'februari'
        hari= 29 if kabisat else 28
    elif bulan== 3:
        nama_bulan='maret'
        hari=31
    elif bulan== 4:
        nama_bulan='april'
        hari=30
    elif bulan== 5:
        nama_bulan='mei'
        hari=31
    elif bulan== 6:
        nama_bulan='juni'
        hari=30
    elif bulan== 7:
        nama_bulan='juli'
        hari=31
    elif bulan== 8:
        nama_bulan='agustus'
        hari=31
    elif bulan== 9:
        nama_bulan='september'
        hari=30
    elif bulan== 10:
        nama_bulan='oktober'
        hari=31
    elif bulan== 11:
        nama_bulan='november'
        hari=30
    elif bulan== 12:
        nama_bulan='desember'
        hari=31
        
    return nama_bulan, hari

ulang= 'y'
while ulang.lower()== 'y':
    bulan=int(input('masukan bulan(1-12):'))
    tahun=int(input('masukan tahun:'))
    
    nama_bulan, hari= jumlah_hari(bulan, tahun)
    
    if hari:
        print(f'\nbulan {nama_bulan},tahun {tahun} ada {hari} hari')
        
        ulang=input('\nmau diulang?(y/t):')
