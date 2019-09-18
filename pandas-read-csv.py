import pandas as pd

filename = 'pmresult.csv'

# membaca file csv, dan ngeskip baris ke 2 dari file
df = pd.read_csv(filename, skiprows=[1])

# menampilkan 10 baris pertama
print('Menampilkan 10 baris pertama')
print(df.head(100))

# menampilkan 10 baris terakhir
print('Menampilkan 10 baris terakhir')
print(df.tail(10))


# menampilkan semua data
print('Menampilkan semua data')
print(df)

# menampilkan kolom Result Time, Object Name dan 73429051
print('Menampilkan kolom Result Time, Object Name dan 73429051')
print(df[['Result Time', 'Object Name', '73429051']])

# menampilkan kolom tertentu + fungsi head
print('Menampilkan kolom Object Name dan 73429051 + menggunakan fungsi head')
print(df[['Object Name','73429051']].head())
