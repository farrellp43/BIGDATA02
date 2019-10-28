# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 09:37:28 2019

@author: Asus
"""

class Segiempat:
    
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar
    
    def Luas(self):
        luas = self.panjang * self.lebar
        print("\nPanjang segiempat =", self.panjang)
        print("Lebar segiempat =", self.lebar)
        print("Luas segiempat =", luas)

a = int(input("Masukkan panjang: "))
b = int(input("Masukkan lebar: "))    
segiempat = Segiempat(a, b)
segiempat.Luas()