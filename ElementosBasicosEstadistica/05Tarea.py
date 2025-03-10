import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el archivo CSV
file_path = "ElementosBasicosEstadistica/housing.csv"
df = pd.read_csv(file_path)

# Columnas de interés
columnas = ["median_house_value", "total_bedrooms", "population"]

# Función para calcular estadísticas descriptivas
def calcular_estadisticas(df, columnas):
    estadisticas = {}
    
    for col in columnas:
        datos = df[col].dropna()  
        estadisticas[col] = {
            "Media": np.mean(datos),
            "Mediana": np.median(datos),
            "Moda": datos.mode()[0],
            "Rango": np.max(datos) - np.min(datos),
            "Varianza": np.var(datos, ddof=1),
            "Desviación Estándar": np.std(datos, ddof=1)
        }
    
    return pd.DataFrame(estadisticas)

# Calcular estadísticas
estadisticas_df = calcular_estadisticas(df, columnas)

# Mostrar estadísticas en tabla
print("Estadísticas Descriptivas:")
print(estadisticas_df)

# Generar tablas de frecuencias
for col in columnas:
    tabla_frecuencia = df[col].value_counts().reset_index()
    tabla_frecuencia.columns = [col, "Frecuencia"]
    print(f"Tabla de Frecuencia - {col}")
    print(tabla_frecuencia.head(10))  # Mostrar solo las primeras 10 filas para no saturar la salida


#  Gráfico de histograma comparativo
plt.figure(figsize=(10, 6))

# Histograma de median_house_value
sns.histplot(df["median_house_value"], bins=30, kde=True, color="blue", label="Median House Value", alpha=0.5)

# Histograma de total_bedrooms
sns.histplot(df["total_bedrooms"], bins=30, kde=True, color="red", label="Total Bedrooms", alpha=0.5)

# Histograma de population
sns.histplot(df["population"], bins=30, kde=True, color="yellow", label="Population", alpha=0.5)

# Título y etiquetas
plt.title("Histograma Comparativo")
plt.xlabel("Valor")
plt.ylabel("Frecuencia")
plt.legend()

#  Mostrar gráfico
plt.show()
