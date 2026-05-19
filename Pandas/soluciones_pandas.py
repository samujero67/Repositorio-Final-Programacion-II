#Clase 1
#Ejercicios:
#1.Calcular el promedio por filas en las filas de indice 10 al 20. Nota: Cuidado con la última columna
df.iloc[10:21,:-1].mean(axis=1)



#---------------------------------------------------
#Clase 2:
#Ejercicios:



#2.Calcular el máximo por fila en las primeras 15 filas, usando solo las 4 columnas numéricas.
df.iloc[0:15,:4].max(axis=1)



#4.Crear una nueva columna llamada ratio_sepal = sepal_length_cm / sepal_width_cm usando iloc para tomar las columnas por posición.
df['ratio_sepal']=df.iloc[:,0]/df.iloc[:,1]



#6.Calcular el promedio de petal_length_cm solo para species == 'setosa'.
df.loc[df['species']=='Iris-setosa','petal_length_cm'].mean()



#8.Contar cuántas filas hay por cada species (usando filtros con loc).
cont_set=len(df.loc[df['species']=='Iris-setosa'])
cont_ver=len(df.loc[df['species']=='Iris-versicolor'])
cont_virgi=len(df.loc[df['species']=='Iris-virginica'])
cont_set,cont_ver,cont_virgi



#10.Multiplicar sepal_width_cm por 10 solo en las filas donde species == 'versicolor' usando loc.
df.loc[df['species']=='Iris-versicolor','sepal_width_cm']=df.loc[df['species']=='Iris-versicolor','sepal_width_cm']*10