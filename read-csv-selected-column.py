import csv

filename = 'pmresult.csv'

csv_file = open(filename, 'r')

csv_reader = csv.reader(csv_file, delimiter = ',')
#dibatasi hanya 10 row
row_count = 0
for row in csv_reader:
    # hanya ngeprint object name
    print(row[2])
    # print(row)
    row_count+=1

    if row_count == 10:
        break
