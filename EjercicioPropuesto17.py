import math


radio = float(input("Ingrese el valor del radio: "))

area_circulo = math.pi * (radio**2)
longitud_circulo = 2*math.pi*radio

print(f"El area del circulo es: {round(area_circulo,2)}")
print(f"El perimetro del circulo es: {round(longitud_circulo,2)}")

