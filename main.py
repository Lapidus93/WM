import pandas as pd
balance = pd.read_csv('balance/basic_comb.csv', sep=';')
print(balance.iloc[:,'':2])
