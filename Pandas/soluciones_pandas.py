#Clase 1
#Ejercicios:
#1.Calcular el promedio por filas en las filas de indice 10 al 20. Nota: Cuidado con la última columna
df.iloc[10:21,:-1].mean(axis=1)


#2.Calcular el máximo por fila en las primeras 15 filas, usando solo las 4 columnas numéricas.
df.iloc[0:15,:4].max(axis=1)


#3.Seleccionar las filas de posición 25 a 35 (incluye 35) y únicamente las columnas de posición 0 y 2.
subset_25_35 = df.iloc[25:36, [0, 2]]


#4.Crear una nueva columna llamada ratio_sepal = sepal_length_cm / sepal_width_cm usando iloc para tomar las columnas por posición.
df['ratio_sepal']=df.iloc[:,0]/df.iloc[:,1]


#5.Poner en 0 el valor de petal_width_cm para las últimas 5 filas usando iloc.
df.iloc[-5:, 3] = 0


#6.Calcular el promedio de petal_length_cm solo para species == 'setosa'.
df.loc[df['species']=='Iris-setosa','petal_length_cm'].mean()


#7.Mostrar las columnas sepal_length_cm y species para las filas donde sepal_length_cm > 6.5.
promedio_setosa = df.loc[df['species'] == 'setosa', 'petal_length_cm'].mean()


#8.Contar cuántas filas hay por cada species (usando filtros con loc).
cont_set=len(df.loc[df['species']=='Iris-setosa'])
cont_ver=len(df.loc[df['species']=='Iris-versicolor'])
cont_virgi=len(df.loc[df['species']=='Iris-virginica'])
cont_set,cont_ver,cont_virgi


#9.Crear una columna petal_area = petal_length_cm * petal_width_cm solo para species == 'virginica' (las demás filas deben quedar como NaN).
df.loc[df['species'] == 'virginica', 'petal_area'] = (
    df['petal_length_cm'] * df['petal_width_cm']
)



#10.Multiplicar sepal_width_cm por 10 solo en las filas donde species == 'versicolor' usando loc.
df.loc[df['species']=='Iris-versicolor','sepal_width_cm']=df.loc[df['species']=='Iris-versicolor','sepal_width_cm']*10


#Clase 2
#Ejercicios: