# -*- coding: utf-8 -*-
"""
Created on Sat May 22 21:48:34 2021

@author: ErgulAslan
"""

#Ergul ASLAN


import pandas as pan, matplotlib.pyplot as plt

veri = pan.read_csv("top50.csv")

veriler = []
isim = []
dans = []
ID = []
energy = []
energyOrt = []
GNum = []

for item in veri.values:
    ID.append(item[0])
    dans.append(item[6])
    if item[3] in isim:
        index = isim.index(item[3])
        veriler[index].append(item)
        energy[index].append(item[5])
        pass
    else:
        veriler.append([item[3], item])
        isim.append(item[3])
        energy([item[5]])
        pass

""" üstteki fordan sonra VERİLER degiskeninin icinde her eleman 1 türün verilerini iceriyor
    veriler[0] ın içinde canadian pop türü var liste şeklinde, ilk elemanlar tür adı
    veriler[0][0] -> türün adı, veriler[0][1] canadian pop'un ilk elemanı ...
"""

for item in veriler:
    baslik = item[0]
    print("--", baslik, " : ")
    for i in item:
        if str(i) != baslik:
            sas = ""
            for j in i:
                if j != i[len(i)-1]:
                    sas += str(j) + ", "
                    pass
                else:
                    sas += str(j)
                    pass
                pass
            print("\t", sas)
            pass
        pass
    print("")
    pass

for i, v in enumerate(energy):
    toplam = 0
    for j in v:
        toplam += j
        pass
    energyOrt.append(toplam/len(v))
    GNum.append((i+1))
    pass

plt.plot(GNum, energyOrt)
plt.xlabel("Grup Numarası")
plt.ylabel("Enerji Ortalaması")
plt.title("Enerji Grafiği")
plt.show()

plt.plot(ID, dans)
plt.xlabel("Şarkı ID")
plt.ylabel("Dans")
plt.title("Dans Grafiği")
plt.show()