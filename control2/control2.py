
import pandas as pd
import math 
from pandas import read_csv, to_numeric
import numpy 
from numpy import nan
import statistics as sta

#df = pd.read_csv('/Users/king/Documents/python/Archive/athlete_events.csv')
fields = ['Height', 'Year', "Sport"]

df = pd.read_csv('/Users/king/Documents/python/Archive/athlete_events.csv', skipinitialspace=True, usecols=fields)

def preprocesamientoDeDatos(df):
    """
    DESCRIPCION:
        Proceso de depurado: eliminacion de registros con datos faltantes 
        y conversion a numericos de las columnas admisibles.
    INPUT:
        @param df: tabla de datos
        @type df: pandas.DataFrame
    OUTPUT:
        @param tabla: tabla de datos
        @type tabla: pandas.DataFrame
    """    
    
    tabla = df.copy()
    
    ## Eliminemos los registros con datos faltantes
    tabla.replace(to_replace='NA', value=nan, inplace=True)
    tabla.replace(to_replace='?', value=nan, inplace=True)
    tabla.dropna(inplace=True)
    
    ## Convertimos las columnas que son "numericas" a numericas
    for col in tabla.columns:
        try:
            to_numeric(tabla[col])
        except:
            error ='Columna: {} no es convertible a numerico'.format(col)
        else:
            tabla[col] = to_numeric(tabla[col])
    
    ## Retornar tabla procesada
    return tabla
tabla_limpia=preprocesamientoDeDatos(df)
# print('Total de Filas original:',df.shape[0])
# print('Total Filas sin NaN:',tabla_limpia.shape[0])
print("")
print("NOTA: Se han limpiado los campos con valores igual a NaN ","quedando de: ",df.shape[0], " a: ",tabla_limpia.shape[0])
print("")
def comparaVectores(a,b):
    if len(a) != len(b):
        return False
    for item_a, item_b in zip(a, b):
        if item_a > item_b:
            return False

    return True

def annosDeporte(disciplina1,disciplina2):
    #Esta función entregará los años del deporte que exista en el archivo.
    annosDeporte =tabla_limpia[tabla_limpia["Sport"]==disciplina1]
    a = numpy.asarray(annosDeporte["Year"].unique())
    print("/--------------------------------Años deporte "+disciplina1+" -----------------------------------/")
    print(numpy.sort(a))
    annosDeporte2 =tabla_limpia[tabla_limpia["Sport"]==disciplina2]
    b = numpy.asarray(annosDeporte2["Year"].unique())
    print()
    print("/--------------------------------Años deporte "+disciplina2+" -----------------------------------/")
    print(numpy.sort(b))
    annosiguales =[]
    contador=0
    res = comparaVectores(a,b)
    if (res == True):
        print("Tienen los mismos años para poder comparar")
    else:
        for i in a:
            valor1=i
            for x in b:
                valor2=x
                if (valor1==valor2):
                    annosiguales.append(valor1)
                    contador=contador+1
    
    print()
    print("/--------------------------------Años a comparar son: -----------------------------------/")
    print(numpy.sort(annosiguales))   
    print("")        
    return annosiguales

def nAynB(disciplina,anno):
    #Esta función entrega el total de jugadores por Disciplina y año
    tabla_deporte=tabla_limpia.loc[(tabla_limpia['Sport'] == disciplina) & (tabla_limpia['Year'] == anno),] 
    totalDeportistas=len(tabla_deporte)
    return totalDeportistas

def alturaPromedio(disciplina,anno):
    # print("El largo del vector es: ",str(len(vectorAnnos)))
    # print("El vector es: ")
    #print(numpy.sort(vectorAnnos))
    tabla_deporte=tabla_limpia.loc[(tabla_limpia['Sport'] == disciplina) & (tabla_limpia['Year'] == anno),] 
    promedio = tabla_deporte["Height"]
    return sta.mean(promedio)

def varianzaPromedio(disciplina,anno):
    #Como dice el enunciado es la varianza promedio de estatura entre los deportistas.
    #Input: Solicitar el nombre de la disciplina
    tabla_deporte=tabla_limpia.loc[(tabla_limpia['Sport'] == disciplina) & (tabla_limpia['Year'] == anno),] 
    varianza = tabla_deporte["Height"]
   # print(tabla_deporte)
    return varianza.var()
    #return sta.variance(varianza)

def listadoDeportes():
    vector_deportes = tabla_limpia["Sport"].unique()
    vector_deportes.sort()
    filas=len(vector_deportes)
    matriz = []
    contador=0
    for x in range(1,filas):
        for y in range (1,2):
            matriz.append((x,vector_deportes[contador]))
            contador=contador+1
    print("/--------------------------------Menú Control 2-----------------------------------/")
    print("/-------------------------------Escoja un número-----------------------------/")
    print
    print(matriz)
    print("/--------------------------------Menú-----------------------------------/")
    #opciones = opciones.split('/')
    #print(vector_deportes)
    #print(len(vector_deportes))
    return matriz

def ecuacionD(XA,XB,VA,VB,NA,NB):
    #Esta ecuación si el valor obtenido esta entre: D < -1.96 y D > 1.96, informará que las estaturas son significativas.
    numerador = XA-XB
    denominador= (VA/NA) +(VB/NB)
    denominador= math.sqrt(denominador)
    d = round(numerador / denominador,4)
    if (d < -1.96 or d > 1.96):
        mensaje="D: "+str(abs(d))+" Hay diferencia significativa"
    else:
        mensaje="D: "+str(abs(d))+" No Hay diferencia significativa"
    return mensaje


matrix=listadoDeportes()
print("")

totalDeportes = len(matrix)
x=True
mensaje="Ingrese el número asociado al primer deporte a evaluar los valores deben estar entre 1 y "+str(totalDeportes)+" donde Taekwondo= 51 y Judo= 28: "
while x==True:
    deporte1=input(mensaje)
    if (deporte1.isdigit()):
        deporte1 = int(deporte1)
        if (deporte1<=totalDeportes and deporte1>0):
            #print(deporte1)
            deporte1 = deporte1-1
            deporte1=matrix[deporte1][1]
            print("UD. Ha escogido el deporte: ",str(deporte1), " El total de deportes son: ",str(totalDeportes))
            while x==True:
                deporte2=input("Escoja el segundo número del deporte a comparar: ")
                if (deporte2.isdigit()):
                    deporte2 = int(deporte2)
                    if (deporte2<=totalDeportes and deporte2>0):
                        deporte2 = deporte2-1
                        deporte2=matrix[deporte2][1]
                        print("UD. Ha escogido el deporte: ",str(deporte2), " UD va a comparar entre: Deporte: ",str(deporte1)," y Deporte : ",str(deporte2))
                        x=False
                    else:
                        print("Debe escoger un número entre 1 y ",str(totalDeportes))    

        else:
            print("Debe escoger un número entre 1 y  SEGUNDO IF",str(totalDeportes))    
    else:
        print("Debe escoger un número entre 1 y PRIMER IF",str(totalDeportes)) 
        
#Ahora obtendremos el promedio XA del primer deporte
year=annosDeporte(deporte1,deporte2)
#Hay que hacer un for por cada año de coincidencias
year.sort()
for i in year:
    xA=alturaPromedio(deporte1,i)
    xB=alturaPromedio(deporte2,i)
    # print("/--------------------------------Año: ",str(i)," -----------------------------------/")
    # print("")
    # print("                               Promedio estatura                                    ")
    # print("La Altura promedio del deporte ",deporte1," xA es: ",str(xA), "y La Altura promedio de",deporte2," xB es: ",str(xB))
    # print("")
    # print("                               Varianza                                           ")
    vA=varianzaPromedio(deporte1,i)
    vB=varianzaPromedio(deporte2,i)
    #print("La Varianza promedio del deporte ",deporte1," vA es: ",str(vA)," y Varianza promedio de",deporte2," vB es: ",str(vB))
    # #print("La Varianza promedio del deporte ",deporte2," vB es: ",str(vB))
    # print("")
    nA=nAynB(deporte1,i)
    nB=nAynB(deporte2,i)
    # print("                               Total deportistas                                           ")
    # print("Para el deporte:  ",deporte1," nA es: ",str(nA)," y para ",deporte2," nA es: ",str(nB))
    # print("")
    # print("                       Existen diferencias significativas?                                           ")
    mensaje=ecuacionD(xA,xB,vA,vB,nA,nB)
    print("Año: ",str(i),mensaje)

print("")
print("NOTA: Se llevo el valor de D al valor absoluto, solamente para evitar incoherencias al desplegar el valor final. Debido a que si uno invierte el orden de las disciplinas (Al momento de ingresar) no debería variar su resultado")

