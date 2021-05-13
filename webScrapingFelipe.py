#Link de ayuda
# Los link de ayuda fueron los siguientes:

# https://pypi.org/project/beautifulsoup4/
# https://brightdata.com/blog/how-tos/how-to-use-beautiful-soup-for-web-scraping-with-python?cam=aw_blog_Beautiful-Soup-web-scraping_web%20scraping%20python_520132069176&utm_term=web%20scraping%20python&utm_campaign=blog&utm_source=adwords&utm_medium=ppc&utm_content=Beautiful-Soup-web-scraping&hsa_acc=1046276282&hsa_cam=13023430270&hsa_grp=124902841831&hsa_ad=520132069176&hsa_src=g&hsa_tgt=kwd-6318385184&hsa_kw=web%20scraping%20python&hsa_mt=b&hsa_net=adwords&hsa_ver=3&gclid=Cj0KCQjws-OEBhCkARIsAPhOkIZd7vbmBkDuQSRsEJgHBE5BGtE4ZEzxHbynDkz_gvdOH8pbS-D2T5MaAjrQEALw_wcB
# https://www.it-swarm-es.com/es/python/extrayendo-el-contenido-de-la-tabla-de-html-con-python-y-beautifulsoup/1072899834/
# https://github.com/MinCiencia/Datos-COVID19/blob/9907f23b69a972f2cb9f217b39e52112ff68004f/output/producto3/CasosTotalesCumulativo.csv

import requests
import pandas as pd
import numpy as np
#datos=urllib.request.urlopen('https://github.com/MinCiencia/Datos-COVID19/blob/9907f23b69a972f2cb9f217b39e52112ff68004f/output/producto3/CasosTotalesCumulativo.csv').read().decode()
url='https://github.com/MinCiencia/Datos-COVID19/blob/9907f23b69a972f2cb9f217b39e52112ff68004f/output/producto3/CasosTotalesCumulativo.csv'
r = requests.get(url)
#print(r.content)
from bs4 import BeautifulSoup
soup = BeautifulSoup(r.content,'html5lib')


def sumarXmes(df):
    #Esta función permite sumar todos los números de casos x mes
    vector_fechas = df["Fecha"].unique()
    largo=len(vector_fechas)
    print('El largo del nuevo arreglo '+str(largo))
    total_enero=0;total_febrero=0;total_marzo=0;total_abril=0;total_mayo=0;total_junio=0;total_julio=0;total_agosto=0;total_septiembre=0
    total_octubre=0;total_noviembre=0;total_diciembre=0
    indice=0
    
    
    for x in vector_fechas:
        dia=x[0:10]
        if (dia =='2020-01-31'): #mes 
            total_enero=total_enero+int(df.iloc[indice]['Total_Casos'])
            #print('total mes dìa : '+x+' '+str(total_mes)+' y el total de casos del día: '+df.iloc[indice]['Total_Casos'])
        if (dia =='2021-02-28'): #mes 
            total_febrero=total_febrero+int(df.iloc[indice]['Total_Casos'])
        if (dia =='2021-03-31'): #mes 
            total_marzo=total_marzo+int(df.iloc[indice]['Total_Casos'])
        if (dia =='2021-04-30'): #mes 
            total_abril=total_abril+int(df.iloc[indice]['Total_Casos'])    
        if (dia =='2021-05-31'): #mes 
            total_mayo=total_mayo+int(df.iloc[indice]['Total_Casos'])    
        if (dia =='2021-06-30'): #mes 
            total_junio=total_junio+int(df.iloc[indice]['Total_Casos'])        
        if (dia =='2021-07-31'): #mes 
            total_julio=total_julio+int(df.iloc[indice]['Total_Casos'])       
        if (dia =='2021-08-31'): #mes 
            total_agosto=total_agosto+int(df.iloc[indice]['Total_Casos'])
        if (dia =='2021-09-30'): #mes 
            total_septiembre=total_septiembre+int(df.iloc[indice]['Total_Casos'])
        if (dia =='2021-10-31'): #mes 
            total_octubre=total_octubre+int(df.iloc[indice]['Total_Casos'])
        if (dia =='2021-11-30'): #mes 
            total_noviembre=total_noviembre+int(df.iloc[indice]['Total_Casos'])   
        if (dia =='2021-12-31'): #mes 
            total_diciembre=total_diciembre+int(df.iloc[indice]['Total_Casos'])                         
        indice=indice +1  
    print('Total casos Enero: '+str(total_enero)+ ' y el total de dìas: '+str(indice))    
    print('Total casos Febrero: '+str(total_febrero)+ ' y el total de dìas: '+str(indice))    
    print('Total casos Marzo: '+str(total_marzo)+ ' y el total de dìas: '+str(indice))    
    print('Total casos Abril: '+str(total_abril)+ ' y el total de dìas: '+str(indice))    
    print('Total casos Mayo: '+str(total_mayo)+ ' y el total de dìas: '+str(indice))    
    print('Total casos Junio: '+str(total_junio)+ ' y el total de dìas: '+str(indice))    
    return 0


#<tr id="LC2" class="js-file-line">
table_santiago=soup.find('tr',attrs = {'id':'LC8'})

#<tr id="LC1" class="js-file-line">
table_fecha=soup.find('tr', attrs={'id':'LC1'})
#print(table_santiago.prettify())

#Recorriendo la tabla de fechas:

fechas=[]
for td in table_fecha.find_all('th'):
    fechas.append(td.text)

# print('Fechas')
# print(fechas)

santiago=[]
for tr in table_santiago.find_all('td'):
    santiago.append(tr.text)

# print(str(len(santiago)))
# print(str(len(fechas)))
# print(santiago[2])
# print(fechas[1])

#Eliminando elementos innecesarios

# santiago.pop(0)
# santiago.pop(1)
# santiago.pop(0)
# fechas.pop(0)

# print('Nuevos totales')
# print(str(len(santiago)))
# print(str(len(fechas)))

#print(str(santiago))

#Creando el dataFrame con los dos vectores
df = pd.DataFrame(list(zip(fechas,santiago)), columns = ['Fecha','Total_Casos'])
casos_porMes=sumarXmes(df)

#Ahora se debe agrupoar por fechas 




