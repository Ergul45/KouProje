# -*- coding: utf-8 -*-
"""
Created on Sat May 15 15:18:57 2021

@author: ErgulAslan
"""


dosya = open("metin2.txt", "r")
veri = dosya.read()
temiz_veri = ""

for i in range(len(veri)):
    if veri[i].isalpha() or veri[i]=='\n':
        temiz_veri+=veri[i]
        
dosya.close()

print(temiz_veri)

dosya=open("temizveri.txt","w")
dosya.write(temiz_veri)
dosya.close()


