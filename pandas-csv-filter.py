import pandas as pd

filename = 'pmresult.csv'

# membaca file csv, dan ngeskip baris ke 2 dari file
df = pd.read_csv(filename, skiprows=[1])

# mencetak data dengan Object Name RNMDN02
print(df[ df['Object Name'].str.startswith('RNMDN02') ])


# coba setelah di filter Object Name nya RNMDN02, yg di cetak kolom Result Time, Object Name dan 73429051
print('------start faishal----------')
dfFiltered = df[ df['Object Name'].str.startswith('RNMDN02') ]  # filter pertama Object Name yang mengandung RNMDN02
dfResult = dfFiltered[dfFiltered['73429051']<150][['Result Time','Object Name','73429051']] # filter kedua nilai pada 73429051 yang kurang dari 150
print(dfResult.head(10)) 
print('------end faishal----------')

# mencetak data dengan object name yang memiliki text MD3G5
print(df[ df['Object Name'].str.contains('MD3G5') ] [['Result Time','Object Name','73429051']])

# mencetak dengan filter object name dan counter value
print(df[ df['Object Name'].str.startswith('RNMDN02') & (df['73429051']<150) ] [['Result Time','Object Name','73429051']])

