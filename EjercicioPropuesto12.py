horas_trabajadas = float(input("Ingrese las horas que realizó el trabajador: "))

valor_hora = float(input("Ingrese el valor de la hora: "))

retencion = 0.125

salario_bruto = horas_trabajadas*valor_hora

salario_neto = salario_bruto - (salario_bruto*retencion)

print(f"El salario bruto es: {salario_bruto}")

print(f"El salario neto es: {salario_neto}")