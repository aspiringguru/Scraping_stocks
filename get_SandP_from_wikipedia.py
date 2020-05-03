import pandas as pd
table=pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
df = table[0]
df.to_csv('data/S&P500-Info.csv', index=False)
df.to_csv("data/S&P500-Symbols.csv", columns=['Symbol'], index=False)
