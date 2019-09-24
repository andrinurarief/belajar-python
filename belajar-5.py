#IF

i = 15
j = 15

#if
if i > j:
    print("i lebih besar dari j")   #baris ini hanya akan di eksekusi jika nilai i lebih besar dari j


#if elif else
if i > j:
    print("i lebih besar dari j")   #baris ini hanya akan di eksekusi jika nilai i lebih besar dari j
elif i < j:
    print("i lebih kecil dari j")
else:
    print("i sama dengan j")

#pertanyaan kuis 1
# buatlah sebuah aplikasi untuk menentukan nilai mahasiswa dalam bentuk index A - E
# dengan ketentuan jika nilai:
# 100 - 90 : A
# 90 - 70  : B
# 70 - 60  : C
# 60 - 40  : D
# 40 - 0   : E
# Jika nilai mahasiswa tidak dalam range 0 - 100, akan muncul pesan kesalahan


#---------------------------------------------------------------------------------------------------
#pertanyaan kuis 2
# buatlah sebuah aplikasi untuk menghitung luas sebuah  bangun datar dengan ketentuan

# aplikasi memiliki 3 buah input yaitu:
# 1. jenis bangun datar
# 2. a
# 3. b

# jenis bangun datar yang di ijinkan untuk di input adalah persegi, persegi panjang, lingkaran, segitiga
# untuk lingkaran, cukup menggunakan input a sebagai jari jari untuk perhitungan luas

# output dari aplikasi adalah luas bangun datar tersebut