import pandas as pd

filename = 'pmresult.csv'

# membaca file csv, dan ngeskip baris ke 2 dari file
df = pd.read_csv(filename, skiprows=[1])

# aggregate kolom
print(df.agg({ '73429051' : ['sum'], '73429056' : ['sum', 'max', 'min', 'mean'], '73429040':['sum', 'max', 'min', 'mean'] }))