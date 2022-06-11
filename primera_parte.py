#-----------------------------------------------------------------------------------------
# Módulos necesarios:
#   PANDAS 0.24.2
#   NUMPY 1.16.3
#
# Para instalar un módulo:
#   Haga clic en el menú File > Settings > Project:nombre_del_proyecto > Project interpreter > botón +
#   Introduzca el nombre del módulo en la zona de búsqueda situada en la parte superior izquierda
#   Elegir la versión en la parte inferior derecha
#   Haga clic en el botón install situado en la parte inferior izquierda
#-----------------------------------------------------------------------------------------


#------------------------------------------
# IMPORTAR LOS MODULOS
#------------------------------------------
import os #Uso del módulo OS (operating system, sistema operativo)


#Uso del módulo Pandas
import pandas as pnd

#Desactivación de la cantidad máxima de columnas del DataFrame a mostrar
pnd.set_option('display.max_columns',None)


#------------------------------------------
# ANALISIS DE LOS DATOS
#------------------------------------------

#Recuperación de los archivos cotenidos en el directorio datas
#de nuestro proyecto
listaDeArchivos = os.listdir("datas")

#¿Cuál es el nombre de cada archivo?
for archivo in listaDeArchivos:
    print(archivo)


#Carga de los datos de los Pokémon en un
#Dataframe llamado nuestrosPokemon
nuestrosPokemon = pnd.read_csv("datas/pokedex.csv")

#Visualización de las columnas del Dataframe
print(nuestrosPokemon.columns.values)

#Visualización de las 10 primeras líneas del DataFrame
print(nuestrosPokemon.head(10))

#Transformación de la columna LEGENDARIO en entero 0= FAlSO y 1=VERDADERO
nuestrosPokemon['LEGENDARIO'] = (nuestrosPokemon['LEGENDARIO']=='VERDADERO').astype(int)
print(nuestrosPokemon['LEGENDARIO'].head(800))


#Recuento de la cantidad de observaciones y características
print (nuestrosPokemon.shape)

#Información de nuestro conjunto de datos
print (nuestrosPokemon.info())

#Búsqueda del nombre del Pokémon que falta
print(nuestrosPokemon[nuestrosPokemon['NOMBRE'].isnull()])
print(nuestrosPokemon['NOMBRE'][61])
print(nuestrosPokemon['NOMBRE'][63])
nuestrosPokemon['NOMBRE'][62] = "Primeape"
print(nuestrosPokemon['NOMBRE'][62])

#Carga de los datos de los combates
combates = pnd.read_csv("datas/combates.csv")

#Visualización de las columnas del Dataframe
print(combates.columns.values)

#Visualización de las 10 primeras líneas del Dataframe
print(combates.head(10))

#Recuento de la cantidad de líneas y de columnas
print (combates.shape)

#Información de nuestro conjunto de datos
print (combates.info())


#Añadir las victorias en primera y segunda posición
nVecesPrimeraPosicion = combates.groupby('Primer_Pokemon').count()
print(nVecesPrimeraPosicion)

nVecesSegundaPosicion = combates.groupby('Segundo_Pokemon').count()
print(nVecesSegundaPosicion)

cantidadTotalDeVictorias = nVecesPrimeraPosicion + nVecesSegundaPosicion
print(cantidadTotalDeVictorias)

cantidadDeVictorias = combates.groupby('Pokemon_Ganador').count()
print(cantidadDeVictorias)


#Se crea una lista a partir de una extracción para obtener la lista de los Pokémon, que se ordenan por número
#Esta lista de números nos permitirá hacer la agregación de los datos
listaAAgregar = combates.groupby('Pokemon_Ganador').count()
listaAAgregar.sort_index()

#Se añade la cantidad de combates
listaAAgregar['N_COMBATES'] = nVecesPrimeraPosicion.Pokemon_Ganador + nVecesSegundaPosicion.Pokemon_Ganador

#Se añade la cantidad de victorias
listaAAgregar['N_VICTORIAS'] = cantidadDeVictorias.Primer_Pokemon

#Se calcula el porcentaje de victorias
listaAAgregar['PORCENTAJE_DE_VICTORIAS']= cantidadDeVictorias.Primer_Pokemon/(nVecesPrimeraPosicion.Pokemon_Ganador + nVecesSegundaPosicion.Pokemon_Ganador)

#Se muestra la lista nueva
print(listaAAgregar)

#Creación de un Pokedex nuevo que contiene los nombres de los Pokemon y su victoria
nuevoPokedex = nuestrosPokemon.merge(listaAAgregar, left_on='NUMERO', right_index = True, how='left')

print(nuevoPokedex)






