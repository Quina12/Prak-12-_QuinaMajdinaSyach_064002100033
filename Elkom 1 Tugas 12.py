# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 23:18:38 2021

@author: Quina
"""

print(" @@@    @   @  @@@  @    @      @@")
print("@   @   @   @   @   @@   @     @  @")
print("@ @ @   @   @   @   @ @  @    @@@@@@")
print("@   @   @   @   @   @  @ @   @      @")
print(" @@@ @  @ @ @  @@@  @    @  @        @")

print("\nLINEAR SEARCH")

import sys

def linearSearch(set, W, Q):
    for i in range(0, W):
        if (set[i] == Q):
            return i
    return -1

number_of_digits = int(input("Masukkan jumlah angka pada List: "))
list_of_numbers = [int(input(f"Angka ke-{i+1}: ")) for i in range(number_of_digits)]
print(f"\nList Angka -> {list_of_numbers}")
ulang = True
while ulang == True:
    find_the_number = int(input("Masukkan angka yang dicari: "))
    for i in list_of_numbers:
        if i == find_the_number:
            print("Hasil Linear Search -> Ditemukan")
            sys.exit()
        else:
            lain = ("\nHASIL Linear SEARCH -> TIDAK DITEMUKAN")
    print(lain)
    ulang = True