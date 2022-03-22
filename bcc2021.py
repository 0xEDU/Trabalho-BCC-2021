#Nesta primeira célula, iremos importar as bibliotecas necessárias para nosso projeto

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

# Importar e mostrar o banco de dados e definir variáveis para facilitar a escrita/leitura
# Dados de 11/03/2020 até 05/12/2021

df = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vRgXJNb_9PF8WaiNrvRAw3ZTzIXcaBOGiXrgWuecR_YrYtBzCMZge6vFsKfUT13dwJsEiJ2W4eLo9JY/pub?output=csv")
pib = df['PIB']
casos = df['Casos']
obitos = df['Obitos']
pop = df['Populacao']
razao = df['Razao caso/letalidade em %']
paises = df['Paises']
df

# Inferências estatíscas sobre população

print(pop)
print("############################")
#Média e mediana
media = pop.mean()
mediana = pop.median()
print("A média de população é ",media,"e a mediana",mediana)

# Inferências estatíscas sobre os casos

print(casos)
print("############################")
#Média e mediana
media = casos.mean()
mediana = casos.median()
print("A média de casos de Covid-19 é ",media,"e a mediana",mediana)

# Medidas de dispersão para casos de Covid-19

#Amplitude, variância e desvio padrão
amp1 = casos.max()-casos.min()
vari = casos.var()
desvpd = casos.std()

print("Os casos tem amplitude de",amp1,)
print("Também há variância de",vari,"e desvio padrão de",desvpd)

# Gráfico 1

plt.plot(obitos,casos,"o")
plt.title("Casos por obito")
plt.grid()

# Correlações entres dados
# Quanto mais perto de 1, mais fortemente positivamente correlacionados são os dados.
# Quanto mais perto de -1, mais fortemente negativamente correlacionados são os dados.
# Quanto mais perto de 0, mais fracamente os dados são relacionados linearmente.


rel1 = pib.corr(casos) 
print("Relação entre casos de Covid-19 e PIB: ", rel1)

rel2 = pop.corr(casos)
print("Relação entre população e casos de Covid-19: ", rel2)

rel3 = pop.corr(razao)
print("Relação entre população e a razão caso/letalidade",rel3)

#Gráfico 2

plt.plot(casos,pib,"o")
plt.title("Casos por PIB")
plt.grid()

#Gráfico 3

plt.plot(pop,casos,"o")
plt.title("População por casos de Covid-19")
plt.grid()

#Gráfico 4

plt.plot(pop,razao,"o")
plt.title("População por razão caso/letalidade")
plt.grid()