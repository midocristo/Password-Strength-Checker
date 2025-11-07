import numpy as np

password = input(str("Input Password: "))
panjangPassword = len(password)

hurufKecil = False
hurufBesar = False
angka = False
simbol = False

for karakter in password:
    if karakter.islower():
        hurufKecil = True
    elif karakter.isupper():
        hurufBesar = True
    elif karakter.isdigit():
        angka = True
    else:
        simbol = True
        
banyakKarakter = 0

if hurufKecil: banyakKarakter += 26
if hurufBesar: banyakKarakter += 26
if angka: banyakKarakter += 10
if simbol: banyakKarakter += 33

print(banyakKarakter)

kombinasi = float(pow(banyakKarakter, panjangPassword))