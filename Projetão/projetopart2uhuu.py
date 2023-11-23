import pandas

df = pandas.read_excel('planilhajogadores.xlsx')

print('############### TABELA COMPLETA ###############\n')
print(df ,'\n')

tabela1 = df.iloc[:, :3]  
tabela2 = df.iloc[:, 2:]  

print('############### TABELAS QUEBRADAS ###############\n')
print(tabela1 ,'\n')
print(tabela2, '\n')

print('############### MERGE ###############\n')

final = pandas.merge(tabela1, tabela2, on="GOLS", how="left")
print(final)
