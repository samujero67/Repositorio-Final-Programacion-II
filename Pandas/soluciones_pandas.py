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
#Ejercicios de Pandas con Iris (Filtrado y creación de columnas)
#Filtrado:
#1.Filtra todas las flores de especie setosa.

setosa = df[df['species'] == 'setosa']


#2.Muestra las filas donde sepal_length sea mayor a 6.0.

sepal_gt_6 = df[df['sepal_length'] > 6.0]


#3.Filtra las flores con petal_length mayor a 4.5 y especie virginica.

virginica_large_petal = df[
    (df['petal_length'] > 4.5) & (df['species'] == 'virginica')
]


#4.Obtén las flores con sepal_width menor a 3.0 y petal_width mayor a 1.0.

filtered_4 = df[
    (df['sepal_width'] < 3.0) & (df['petal_width'] > 1.0)
]


#5.Filtra las filas con petal_length entre 1.5 y 5.0.

between_values = df[
    (df['petal_length'] >= 1.5) & (df['petal_length'] <= 5.0)
]

#Creación de columnas:
#6.Crea una columna sepal_area = sepal_length * sepal_width.

df['sepal_area'] = df['sepal_length'] * df['sepal_width']


#7.Crea una columna petal_area = petal_length * petal_width.

df['petal_area'] = df['petal_length'] * df['petal_width']


#8.Crea una columna petal_sepal_ratio = petal_length / sepal_length.

df['petal_sepal_ratio'] = df['petal_length'] / df['sepal_length']


#9.Crea una columna is_large_sepal que sea True si sepal_length > 5.8, y False en otro caso.

df['is_large_sepal'] = df['sepal_length'] > 5.8


#10.Crea una columna size_category con:
#small si petal_length < 2
#medium si petal_length está entre 2 y 5
#large si petal_length > 5

def categorize(petal_length):
    if petal_length < 2:
        return 'small'
    elif petal_length <= 5:
        return 'medium'
    else:
        return 'large'

df['size_category'] = df['petal_length'].apply(categorize)


#Combinadas (filtrado + nuevas columnas):
#11.Con sepal_area, filtra las flores con área de sépalo mayor al promedio.

mean_sepal_area = df['sepal_area'].mean()
large_sepal_area = df[df['sepal_area'] > mean_sepal_area]


#12.Con petal_area, calcula el promedio por especie.

mean_petal_area_by_species = df.groupby('species')['petal_area'].mean()


#13.Con petal_sepal_ratio, filtra las flores en el percentil 75 o superior.

p75 = df['petal_sepal_ratio'].quantile(0.75)
high_ratio = df[df['petal_sepal_ratio'] >= p75]


#14.Con is_large_sepal, compara cuántas flores hay por especie (groupby).

large_sepal_count = df.groupby('species')['is_large_sepal'].sum()


#15.Con size_category, filtra solo large y calcula la media de petal_width por especie.


large_flowers = df[df['size_category'] == 'large']
mean_petal_width_large = large_flowers.groupby('species')['petal_width'].mean()
