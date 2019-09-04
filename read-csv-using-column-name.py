import csv

filename = 'pmresult.csv'

csv_file = open(filename, 'r')

csv_reader = csv.DictReader(csv_file, delimiter = ',')
#dibatasi hanya 10 row

row_count = 0
csv_reader.__next__()

for row in csv_reader: 
    row_count+=1
    print(row)
    if row_count == 10:
        break
