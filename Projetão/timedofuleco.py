import random
import pandas as pd

gols = [random.randint(0, 10) for _ in range(20)]

faltas = [random.randint(0, 5) for _ in range(20)]

data_gols = {"Gols": gols}
df_gols = pd.DataFrame(data_gols)

maximo_gols = df_gols["Gols"].max()
minimo_gols = df_gols["Gols"].min()
media_gols = df_gols["Gols"].mean()

print("Estatísticas dos Gols:")
print(f"Valor máximo de gols: {maximo_gols}")
print(f"Valor mínimo de gols: {minimo_gols}")
print(f"Média de gols: {media_gols}")


data_faltas = {"Faltas": faltas}
df_faltas = pd.DataFrame(data_faltas)

maximo_faltas = df_faltas["Faltas"].max()
minimo_faltas = df_faltas["Faltas"].min()
media_faltas = df_faltas["Faltas"].mean()


print("\nEstatísticas das Faltas:")
print(f"Valor máximo de faltas: {maximo_faltas}")
print(f"Valor mínimo de faltas: {minimo_faltas}")
print(f"Média de faltas: {media_faltas}")

data = {"Gols": gols, "Faltas": faltas}
df_gols_e_faltas = pd.DataFrame(data)


print("\nGols:")
print(df_gols)

print("\nFaltas:")
print(df_faltas)

print("\nGols e Faltas:")
print(df_gols_e_faltas)

