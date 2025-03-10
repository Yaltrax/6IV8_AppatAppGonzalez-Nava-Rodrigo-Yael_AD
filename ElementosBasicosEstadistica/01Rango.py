import pandas as pd

## programa que pregunte al usuario pro la sventas de un rango de años y muestre en la pantalla la serie de datos las series indexadas por los años,. antes y despues de aplicarles un descuento

inicio = int(input("Introduce el año de ventas imicial:"))
fin = int(input("Introduce el año final de ventas:"))

ventas = {}

for i in range(inicio, fin+1):
    ventas[i] = float(input("Introduce las vemtas del año: " + str(i)
    + ": "))
    
ventas = pd.Series(ventas)
print("Ventas \n" , ventas)
print("Ventas con Descuento\n", ventas*0.9)