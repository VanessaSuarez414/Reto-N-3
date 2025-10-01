num_meses = int(input("¿Cuántos meses desea analizar?: "))

total = 0
mayor_gasto = 0
menor_gasto = 0
mes_mayor = 0
mes_menor = 0

for i in range(1, num_meses + 1):
    gasto = float(input(f"Ingrese el gasto del mes {i}: "))
    total += gasto

    if i == 1:
        mayor_gasto = gasto
        menor_gasto = gasto
        mes_mayor = i
        mes_menor = i
    else:
        if gasto > mayor_gasto:
            mayor_gasto = gasto
            mes_mayor = i
        if gasto < menor_gasto:
            menor_gasto = gasto
            mes_menor = i

promedio = total / num_meses
diferencia = mayor_gasto - menor_gasto

print("\n--- RESULTADOS ---")
print(f"Gasto total: {total} pesos")
print(f"Promedio mensual: {promedio:.2f} pesos")
print(f"Mes con mayor gasto: Mes {mes_mayor} (${mayor_gasto})")
print(f"Mes con menor gasto: Mes {mes_menor} (${menor_gasto})")
print(f"Diferencia entre mayor y menor gasto: {diferencia}")

