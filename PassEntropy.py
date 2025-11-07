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

kombinasi = float(pow(banyakKarakter, panjangPassword))
password_entropy = np.round(np.log2(kombinasi))

if (password_entropy>= 0 and password_entropy <= 35) :
    print("Your Password is Very Weak!")
elif (password_entropy >= 36 and password_entropy <= 59) :
    print("Your Password is Weak!")
elif (password_entropy >= 60 and password_entropy <= 119) :
    print("Your Password is Strong!")
elif (password_entropy >= 120) :
    print("Your Password is Very Strong!")
else :
    print("error!")
    
waktu = kombinasi / 10000000  # misal kombinasi = banyakKarakter ** panjangPassword

if waktu < 1:
    print("It will take less than 1 second to guess!")
elif waktu < 60:
    print("It will take {:.1f} seconds to guess!".format(waktu))
else:
    waktu /= 60
    if waktu < 60:
        print("It will take {:.1f} minutes to guess!".format(waktu))
    else:
        waktu /= 60
        if waktu < 24:
            print("It will take {:.1f} hours to guess!".format(waktu))
        else:
            waktu /= 24
            if waktu < 31:
                print("It will take {:.1f} days to guess!".format(waktu))
            else:
                waktu /= 31
                if waktu < 12:
                    print("It will take {:.1f} months to guess!".format(waktu))
                else:
                    waktu /= 12
                    if waktu < 1000:
                        print("It will take {:.1f} years to guess!".format(waktu))
                    else:
                        waktu /= 1000
                        if waktu < 1000:
                            print("It will take {:.1f} thousand years to guess!".format(waktu))
                        else:
                            waktu /= 1000
                            if waktu < 1000:
                                print("It will take {:.1f} million years to guess!".format(waktu))
