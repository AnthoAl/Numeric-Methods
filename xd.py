error = 1
num_terminos = 0
suma = 0

while error >= 0.1:
    suma += (1/2)**num_terminos
    num_terminos += 1
    error = abs(2 - suma)

print(f"Suma de valores: {suma:.4f}")
print(f"Número de terminos usados: {num_terminos}")
print(f"Error absoluto obtenido: {error:.4f}")

import random

def swap(v1,j):
    v1[j], v1[j - 1] = v1[j-1],v1[j]
    return v1

v1 = [random.randint(-200, 145) for _ in range(10)]

for i in range(len(v1)):
    swapped = False
    for j in range(1,len(v1)-i):
        if (v1[j] < v1[j-1]):
            swap(v1,j)
            swapped = True
    
    if not(swapped):
        break

print("Primeros 20 elementos ordenados:", v1[:20])

import matplotlib.pyplot as plt

def fibonacci(n):
    if n == 0:
        return [0]   # devolvemos lista
    else:
        x = 0
        y = 1
        secuencia = [x, y]  # guardamos los dos primeros valores
        
        for i in range(n-2):  # ya tenemos dos términos
            z = x + y
            x = y
            y = z
            secuencia.append(y)  # guardamos el nuevo valor
    
    return secuencia  # devolvemos la lista completa

# Valor de n
n = 15
secuencia_fib = fibonacci(n)

print("Número de iteraciones:", n)
print("Serie obtenida:", secuencia_fib)
print("Último valor:", secuencia_fib[-1])

# Graficar la secuencia
plt.figure(figsize=(8, 4))
plt.plot(secuencia_fib, marker='o', linestyle='-', color='b')
plt.title('Serie de Fibonacci')
plt.xlabel('Índice')
plt.ylabel('Valor')
plt.grid(True)
plt.show()


import matplotlib.pyplot as plt

def fibonacci(n):
    if n == 0:
        return [0]
    else:
        x = 0
        y = 1
        secuencia = [x, y]
        
        for i in range(n - 2):
            z = x + y
            x = y
            y = z
            secuencia.append(y)
    
    return secuencia

# Número de términos
n = 15
fib = fibonacci(n)

# Calcular los cocientes fib(n)/fib(n-1)
cocientes = []
for i in range(2, len(fib)):  # desde el tercer término
    cociente = fib[i] / fib[i - 1]
    cocientes.append(cociente)

# Mostrar resultados
print("Serie de Fibonacci:", fib)
print("Cocientes (fib(n)/fib(n-1)):", cocientes)

# Graficar los cocientes
plt.figure(figsize=(8, 4))
plt.plot(range(2, n), cocientes, marker='o', linestyle='-', color='orange', label='fib(n)/fib(n−1)')
plt.axhline(y=1.618, color='red', linestyle='--', label='Número áureo ≈ 1.618')
plt.title('Aproximación al Número Áureo usando la Serie de Fibonacci')
plt.xlabel('n')
plt.ylabel('Cociente fib(n)/fib(n−1)')
plt.legend()
plt.grid(True)
plt.show()