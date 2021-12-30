# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 11:09:48 2021

@author: Quina
"""

print(" @@@    @   @  @@@  @    @      @@")
print("@   @   @   @   @   @@   @     @  @")
print("@ @ @   @   @   @   @ @  @    @@@@@@")
print("@   @   @   @   @   @  @ @   @      @")
print(" @@@ @  @ @ @  @@@  @    @  @        @")

print("\nBUBBLE SORT")

def bubble_sort(set):
  for i in range(len(set)):
    for Q in range(0, len(set) - i - 1):
      if set[Q] > set[Q + 1]:
        temp = set[Q]
        set[Q] = set[Q+1]
        set[Q+1] = temp

number_of_digits = int(input("Masukkan jumlah angka pada List: "))
list_of_numbers = [int(input(f"Angka ke-{i+1}: ")) for i in range(number_of_digits)]
print(f"\nList Angka -> {list_of_numbers}")
bubble_sort(list_of_numbers)
print(f"Hasil Bubble Sort -> {list_of_numbers}")