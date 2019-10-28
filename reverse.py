# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 10:20:05 2019

@author: Asus
"""

class Reverse:
    
    def __init__(self, kalimat):
        self.kalimat = kalimat
    
    def balik(self):
        x = self.kalimat
        print("Kalimat setelah dibalik =", x[::-1])
    
a = input("Masukkan kalimat yang ingin dibalik = ")
reverse = Reverse(a)
reverse.balik()