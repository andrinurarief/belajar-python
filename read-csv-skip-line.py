import csv

filename = 'pmresult.csv'

csv_file = open(filename, 'r')

csv_reader = csv.reader(csv_file, delimiter = ',')
#dibatasi hanya 10 row

#isal
# row_count = 0
# for row in csv_reader: 
#     if row[0] == '':   
#         continue
        
#     print(row)
#     row_count+=1

#     if row_count == 10:
#         break

#fathur
# row_count = 0
# for row in csv_reader:
    
#     row_count+=1

#     if row_count == 2:
#         continue
    
#     print(row)

#     if row_count == 10:
#         break

#enumerate
for x,row in enumerate(csv_reader,1):
    if x != 2 :
        print(row)
    
    if x == 10:
        break
