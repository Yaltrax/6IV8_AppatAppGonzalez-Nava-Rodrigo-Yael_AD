import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv("ElementosBasicosEstadistica/housing.csv")

# Mostrar las primeras 5 filas
print(df.head())

# Mostrar las últimas 5 filas
print(df.tail())

# Mostrar una fila en específico
print(df.iloc[7])

# Mostrar la columna ocean_proximity
print(df["ocean_proximity"])

# Obtener la media de la columna total_rooms
media_total_rooms = df["total_rooms"].mean()
print(f"La media de total rooms es: {media_total_rooms}")

# Obtener la mediana de la columna median_house_value
mediana_house_value = df["median_house_value"].median()
print(f"La mediana de la columna median_house_value es: {mediana_house_value}")

# Obtener la suma de la población
suma_poblacion = df["population"].sum()
print(f"La suma total de la población es: {suma_poblacion}")

# Para poder filtrar los datos donde ocean_proximity sea "ISLAND"
filtro_island = df[df["ocean_proximity"] == "ISLAND"]
print(filtro_island)

# Convertir la columna categórica 'ocean_proximity' a valores numéricos
df["ocean_proximity_num"], labels = pd.factorize(df["ocean_proximity"])

# Crear un gráfico de dispersión
plt.figure(figsize=(8, 5))
plt.scatter(df["ocean_proximity_num"].head(100), df["median_house_value"].head(100), alpha=0.5)

# Nombrando los ejes
plt.xlabel("Proximidad al océano (Codificada)")
plt.ylabel("Precio de la casa")

# Título del gráfico
plt.title("Gráfico de Dispersión: Proximidad al Océano vs Precio")

# Mostrar etiquetas en el eje X
plt.xticks(ticks=range(len(labels)), labels=labels, rotation=45)

# Mostrar el gráfico
plt.show()
