# -*- coding: utf-8 -*-
"""
Created on Wed Oct 29 22:31:09 2025

@author: khairunnajmi hibrizi
"""

def angka(nilai):
    nilai = nilai.upper()
    if nilai =='A':        
        return 4.0
    elif nilai == 'A-':
        return 3.75
    elif nilai =='B+':
        return 3.5
    elif nilai =='B':
        return 3.00
    elif nilai =='B-':
        return 2.75
    elif nilai =='C+':
        return 2.5
    elif nilai =='C':
        return 2.0
    elif nilai =='C-':
        return 1.75
    elif nilai =='D':
        return 1.5
    

daftar_nilai = []

while True:
    masukan = input("Masukkan nilai huruf (enter untuk keluar): ")
    if masukan == "":
        break

    nilai_angka = angka(masukan)
    print("Nilai angka:", nilai_angka)
    daftar_nilai.append(nilai_angka)

if daftar_nilai:
    nilai_rata = sum(daftar_nilai) / len(daftar_nilai)
    print(f"\nRata-rata angka: {nilai_rata:.2f}")
else:
    print("Tidak ada nilai yang dimasukkan.")