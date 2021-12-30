# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 13:19:38 2021

@author: Quina
"""

print(" @@@    @   @  @@@  @    @      @@")
print("@   @   @   @   @   @@   @     @  @")
print("@ @ @   @   @   @   @ @  @    @@@@@@")
print("@   @   @   @   @   @  @ @   @      @")
print(" @@@ @  @ @ @  @@@  @    @  @        @")

print("\nSELECTION SORT")

def selection_sort(W):
    for i in range(len(W)-1):
        min_index = i
        for Q in range(i+1, len(W)):
            if W[Q] < W[min_index]:
                min_index = Q
        W[i], W[min_index] = W[min_index], W[i]
        
number_of_digits = int(input("Masukkan jumlah angka pada List: "))
list_of_numbers = [int(input(f"Angka ke-{i+1}: ")) for i in range(number_of_digits)]
print(f"\nList Angka -> {list_of_numbers}")
selection_sort(list_of_numbers)
print(f"Hasil Selection Sort -> {list_of_numbers}")