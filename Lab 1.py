# Problema 1

capital = 100  # Monto inicial de la inversión
tasa_interes = 0.10  # Tasa de interés anual

for _ in range(7):
    capital = capital * (1 + tasa_interes)

print("El resultado después de 7 años de inversión es de", capital, "dólares.")

# problema 2

ahorros = 100  # Monto de ahorros

print("El valor de ahorros es:", ahorros)

# problema 3

# Crear la variable ahorros y asignarle el valor de 100
ahorros = 100

# Crear la variable multiplicador anual
mult_anual = 1.1

# Calcular el resultado del interés compuesto
resultado = ahorros * mult_anual ** 7

# Imprimir el resultado
print("El resultado después de 7 años de inversión es de", resultado)
# problema 4

desc = "cadena de texto"  # Variable de tipo string
profit = True  # Variable booleana con valor True

print("desc:", desc)
print("profit:", profit)

# problema 5

ahorros = 100  # Monto de los ahorros
multiplicador = 1.5  # Valor del multiplicador

año = ahorros * multiplicador

print("El resultado del producto de los ahorros y el multiplicador es:", año)

# problema 6

ahorros = 100
resultado = 100 * 1.1**7

# Corregir la impresión
print("Empezamos con $" + str(ahorros) + " y ahora mismo tengo $" + str(resultado) + ". ¡Qué bien!")