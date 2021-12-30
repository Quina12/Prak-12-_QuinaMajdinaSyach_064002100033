# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 09:51:17 2021

@author: Quina
"""

print(" @@@    @   @  @@@  @    @      @@")
print("@   @   @   @   @   @@   @     @  @")
print("@ @ @   @   @   @   @ @  @    @@@@@@")
print("@   @   @   @   @   @  @ @   @      @")
print(" @@@ @  @ @ @  @@@  @    @  @        @")

print("\nBINARY SEARCH")

import sys

def binarySearch(set, W, low, high):
    while low <= high:
        mid = low + (high - low)//2
        if set[mid] == W:
            return mid
        elif set[mid] < W:
            low = mid + 1
        else:
            high = mid - 1
    return -1

number_of_digits = int(input("Masukkan jumlah angka pada List: "))
list_of_numbers = [int(input(f"Angka ke-{i+1}: ")) for i in range(number_of_digits)]
print(f"\nList Angka -> {list_of_numbers}")
ulang = True
while ulang == True:
    find_the_number = int(input("Masukkan angka yang dicari: "))
    for i in list_of_numbers:
        if i == find_the_number:
            print(f"Hasil Binary Search -> Ditemukan ( di index {list_of_numbers.index(i)} )")
            sys.exit()
        else:
            lain = ("\nHASIL BINARY SEARCH -> TIDAK DITEMUKAN" "\nSILAHKAN MASUKKAN KEMBALI")
    print(lain)
    ulang = True