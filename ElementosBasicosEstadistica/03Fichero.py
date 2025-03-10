import pandas as pd

def resumen_cotizacion(fichero):
    df = pd.read_csv(fichero, sep=";", decimal=",", index_col=0)
    
    df = df.apply(pd.to_numeric, errors='coerce')

    resumen = pd.DataFrame({ "Min": df.min(), "Max": df.max(), "Media": df.mean(), "Desviacion Estandar": df.std() }).T

    return resumen

print(resumen_cotizacion("./ElementosBasicosEstadistica/cotizacion.csv"))
