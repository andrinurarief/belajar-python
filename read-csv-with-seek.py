import csv

row_count = 0

filename = 'pmresult.csv'

csv_file = open(filename, 'r')

csv_reader = csv.reader(csv_file, delimiter = ',')
# csv_list = list(csv_reader)

for row in csv_reader:

    print(row)
    row_count+=1

    if row_count == 2:
        break

row_count = 0
csv_file.seek(0, 0)
for row in csv_reader:

    print(row)
    row_count+=1

    if row_count == 2:
        break