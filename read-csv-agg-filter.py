import csv

filename = 'pmresult.csv'

csv_file = open(filename, 'r')

#DictReader untuk skip baris pertama
csv_reader = csv.DictReader(csv_file, delimiter = ',')

#skip baris kedua file csv (bergantung pada isi csv)
csv_reader.__next__() #untuk membaca baris selanjutnya

total = {}
for row in csv_reader:
    if 'RNMDN02' in row['Object Name']:
        if 'RNMDN02' not in total:
            total['RNMDN02'] = 0

        total['RNMDN02'] += int(row['73429039'])

print("Total kolom '73429039' : " + str(total))

