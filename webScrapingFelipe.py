import requests
import pandas as pd
import numpy as np
#datos=urllib.request.urlopen('https://github.com/MinCiencia/Datos-COVID19/blob/9907f23b69a972f2cb9f217b39e52112ff68004f/output/producto3/CasosTotalesCumulativo.csv').read().decode()
url='https://github.com/MinCiencia/Datos-COVID19/blob/9907f23b69a972f2cb9f217b39e52112ff68004f/output/producto3/CasosTotalesCumulativo.csv'
r = requests.get(url)
#print(r.content)
from bs4 import BeautifulSoup
soup = BeautifulSoup(r.content,'html5lib')

#<tr id="LC2" class="js-file-line">
table_arica=soup.find('tr',attrs = {'id':'LC2'})

#<tr id="LC1" class="js-file-line">
table_fecha=soup.find('tr', attrs={'id':'LC1'})
#print(table_arica.prettify())

#Recorriendo la tabla de fechas:

fechas=[]
for td in table_fecha.find_all('th'):
    fechas.append(td.text)

# print('Fechas')
# print(fechas)

arica=[]
for tr in table_arica.find_all('td'):
    arica.append(tr.text)

print(str(len(arica)))
print(str(len(fechas)))
# print(arica[2])
# print(fechas[1])

#Eliminando elementos innecesarios

arica.pop(0)
arica.pop(1)
fechas.pop(0)

print('Nuevos totales')
print(str(len(arica)))
print(str(len(fechas)))

#print(str(arica))

#Creando el dataFrame con los dos vectores
df = pd.DataFrame(list(zip(fechas,arica)), columns = ['Fecha','Total_Casos'])
print(df)
