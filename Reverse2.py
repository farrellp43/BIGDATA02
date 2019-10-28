# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 10:32:42 2019

@author: Asus
"""

class Reverse2:
    
    def __init__(self, kalimat):
        self.kalimat = kalimat
    
    def balik(self):
        splitKata = self.kalimat.split(" ")
        splitKata = splitKata[::-1]
        y = " ".join(splitKata)
        print("Kalimat setelah dibalik =", y)
    
a = input("Masukkan kalimat yang ingin dibalik = ")
reverse = Reverse2(a)
reverse.balik()