import csv

filename = 'pmresult.csv'

csv_file = open(filename, 'r')

csv_reader = csv.reader(csv_file, delimiter = ',')

#dibatasi hanya 10 row
row_count = 0 #biar mudah mengenali kalo ini buat counternya
for row in csv_reader:

    print(row)
    row_count+=1

    if row_count == 10:
        break