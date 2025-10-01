num_meses = int(input("¿Cuántos meses desea analizar?: "))
gastos = []
for i in range(num_meses):
    gasto = float(input(f"Ingrese el gasto del mes {i+1}: "))
    gastos.append(gasto)
total = 0
for g in gastos:
    total += g
mayor_gasto = gastos[0]
mes_mayor = 1
for i in range(num_meses):
    if gastos[i] > mayor_gasto:
        mayor_gasto = gastos[i]
        mes_mayor = i + 1
menor_gasto = gastos[0]
mes_menor = 1
for i in range(num_meses):
    if gastos[i] < menor_gasto:
        menor_gasto = gastos[i]
        mes_menor = i + 1
promedio = total / num_meses
diferencia = mayor_gasto - menor_gasto
print("\n--- RESULTADOS ---")
print(f"Gasto total: {total} pesos")
print(f"Promedio mensual: {promedio:.2f} pesos")
print(f"Mes con mayor gasto: Mes {mes_mayor} (${mayor_gasto})")
print(f"Mes con menor gasto: Mes {mes_menor} (${menor_gasto})")
print(f"Diferencia entre mayor y menor gasto: {diferencia}")
