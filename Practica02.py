import random
import time
import matplotlib.pyplot as plt

def genArreglos(tamaño):
    return [random.randint(1, 1000) for _ in range(tamaño)]

def printArreglos(array, label):
    print(label, array)

def quicksort(array):
    if len(array) <= 1:
        return array

    pivote = sum(array) // len(array)
    left = []
    right = []
    igual = []

    for elemento in array:
        if elemento < pivote:
            left.append(elemento)
        elif elemento > pivote:
            right.append(elemento)
        else:
            igual.append(elemento)

    return quicksort(left) + igual + quicksort(right)

def tiempoArreglos(array):
    start_time = time.time()
    arregloOrd = quicksort(array)
    end_time = time.time()
    return arregloOrd, end_time - start_time

tamaños = []
tiempos = []

for i in range(10, 101):
    array = genArreglos(i)
    printArreglos(array, "Arreglo desordenado:")
    
    arregloOrd, timpoOrdenado = tiempoArreglos(array)
    printArreglos(arregloOrd, "Arreglo ordenado:")
    
    tamaños.append(i)
    tiempos.append(arregloOrd)

plt.plot(tamaños, tiempos, marker='o', linestyle='-')
plt.title('Tiempos de ordenamiento')
plt.xlabel('Tamaño del Arreglo')
plt.ylabel('Tiempo (segundos)')
plt.grid(True)
plt.show()
