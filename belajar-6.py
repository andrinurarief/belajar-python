# for x in range(1, 101):
#     print(x)
    

# for x in range(2,101):
#     if x % 2 == 0:
#         print(x)

# for x in range(2, 101, 2):
#     print(x)

#jawaban dari pertanyaan faisal, range di simpan di dalam variable
# var = range(2, 101, 2)
# for x in var:
#     print(x)

# name = 'faishal'
# for kar in name:
#     print(kar)

nama = 'faishal'
for x,y in enumerate(nama,1):
    if x % 2 == 0:
        print(y)

counter=1
for elem in nama:
    if counter % 2 == 0:
        print (elem)
        counter += 1

for kar in nama:
    index = nama.index(kar)
    if index % 2 != 0:
        print(kar)

for i in range(len(nama)):
    if(i % 2) == 1:
        print(kar[i])


'''

ada pertanyaan?
fungsi 2 dibelakang itu buat apa? 
buat stepnya om pei
jadi penambahan nya 2
kalau penambahannya mau 3, di parameter terakhir 2 nya di ganti 3

selain cara di atas, bisa juga menambahkan parameter step di fungsi range
paramter 3 dari fungsi range bisa di isi dengan step dari perulangannya, defaultnya adalah 1

for di gunakan untuk mengulangi eksekusi baris kode dengan jumlah perulangan tertentu
misal, kita ingin mencetak angka 1 - 100
jika tanpa perulangan, harus menulis kode print(1) sampai dengan print(100)
dengan menggunakan perulangan for, cukup di tulis dengan 2 baris kode
fungsi range pada baris pertama adalah untuk membuat array dengan nilai 1 - 100

kemudian di lakukan perulangan, setiap perulangan di simpan di dalam vaiable x

kemudian variable x di print

#soal 1
coba buat program
untuk mencetak bilangan genap dari 2 - 100
menggunakan for dan if

untuk om pei bisa coba untuk buat programmnya langsung di editor ini
di baris ke 5 aja mulainya

repot nih klo ga bisa ditest di lokal dlu hueheheh
om pei kurang tanda : setelah for dan if
kurang identasi
dan kurang pengecekan modulus 2 nya

tapi dari logic nya udah dapet

'''
