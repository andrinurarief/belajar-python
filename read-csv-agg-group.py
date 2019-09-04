import csv

filename = 'pmresult.csv'

csv_file = open(filename, 'r')

#DictReader untuk skip baris pertama
csv_reader = csv.DictReader(csv_file, delimiter = ',')

#skip baris kedua file csv (bergantung pada isi csv)
csv_reader.__next__() #untuk membaca baris selanjutnya

total = {}
for row in csv_reader:
    rncname = row['Object Name'].split("/")[0]

    if rncname not in total:
        total[rncname] = 0

    total[rncname] += int(row['73429039'])
    # pass

print("Total kolom '73429039' : " + str(total))

