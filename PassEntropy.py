import numpy

password = input(str("Input Password: "))
panjangPassword = len(password)

hurufKecil = False
hurufBesar = False
angka = False
simbol = False

for karakter in range(panjangPassword):
    if karakter == karakter.lower():
        hurufKecil = True
    elif karakter == karakter.upper():
        hurufBesar = True
    elif karakter.isdigit():
        angka = True
    else:
        simbol = True