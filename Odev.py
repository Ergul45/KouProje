# -*- coding: utf-8 -*-
"""
Created on Fri May  7 13:33:27 2021

@author: ErgulAslan
"""

#1.Soru
print("Lütfen Bir Sayı Giriniz..")
sayi1 = int(input())
if sayi1%2==0:
    print("{} Girdiğiniz Sayi Çifttir".format(sayi1))
else:
    print("{} Girdiğiniz Sayi Tektir.".format(sayi1))
   

#2.Soru
print("\nLütfen 5 sayı giriniz")
SayiListe = []
for i in range(5):
    print(i+1,". sayıyı giriniz : ")
    sayi = int(input())
    SayiListe.append(sayi)

sayac = 0
for i in range(5):
    if SayiListe[i] < 2:
        print(i + 1, ". sayı(", SayiListe[i], ") asal değildir.")
        continue

    for j in range(2, SayiListe[i]):
        if SayiListe[i] % j == 0:
            print(i+1, ". sayı(", SayiListe[i], ") asal değildir.")
            sayac = 1
            break

    if sayac == 0:
        print(i + 1, ". sayı(", SayiListe[i], ") asaldır.")
    sayac = 0
    

#3.Soru

def TemizVeri(ilk_str, ikinci_str, ucuncu_str):
    temizVeri = ""
    for i in range(len(ilk_str)):
        if not ilk_str[i].isdigit():
            temizVeri += ilk_str[i]
    temizVeri += "-"

    for i in range(len(ikinci_str)):
        if not ikinci_str[i].isdigit():
            temizVeri += ikinci_str[i]
    temizVeri += "-"

    for i in range(len(ucuncu_str)):
        if not ucuncu_str[i].isdigit():
            temizVeri += ucuncu_str[i]

    return temizVeri

print("\n", TemizVeri("Ah5me4t", "M9eHm4eT", "Ha3K5a1n"))