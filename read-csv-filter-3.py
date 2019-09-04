import csv

filename = 'pmresult.csv'

csv_file = open(filename, 'r')

#DictReader untuk skip baris pertama
csv_reader = csv.DictReader(csv_file, delimiter = ',')

#skip baris kedua file csv (bergantung pada isi csv)
csv_reader.__next__() #untuk membaca baris selanjutnya

label = ['MD3G57864','MD3G59123','MD3G37231']

ulang = 0
print("Jawaban 3")
#jawaban 3 loop csv baru label dan menggunakan fungsi break
for row in csv_reader:
    for x in label:
        if x in row['Object Name']:
            print(row['Object Name'])
            break
        ulang+= 1
print("Jumlah perulangan Jawaban 3 " + str(ulang))
print("")
