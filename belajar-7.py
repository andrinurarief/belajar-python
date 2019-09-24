'''
misal saya masukan nilai n = 5
output yg di kehendaki

*
**
***
****
*****

kalau nilai n = 4

*
**
***
****

coba buat programnya menggunakan for

'''

print("fathur")
# fathur
n=4
for x in range(n):
    print('*' * (x+1))


print("faishal")
# faishal
i = 5

bintang = []
for x in range(i+1):
    star = '*'
    bintang.append(star)

for x in range(i+1):
    print(''.join(bintang[0:x]))

print("ombay")
# ombay
n = int(input("Masukan angka: "))
for x in range (n):
    print((x+1) * "")

    