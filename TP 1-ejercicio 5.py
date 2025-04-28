import random
import time
from typing import List, Callable

# Función para medir el tiempo de ejecución de un algoritmo de ordenamiento
def measure_execution_time(sort_function: Callable[[List[int]], List[int]], lst: List[int]) -> float:
    start_time = time.perf_counter()
    sort_function(lst)
    end_time = time.perf_counter()
    return end_time - start_time

# Algoritmos de ordenamiento
def bubble_sort(arr: List[int]) -> None:
    """
    Ordenamiento por burbuja (in-place). Modifica la lista original.
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def quicksort(arr: List[int]) -> List[int]:
    """
    Implementación de QuickSort. Retorna una nueva lista ordenada.
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Generación de listas aleatorias
def generate_random_list(size: int) -> List[int]:
    """
    Genera una lista de números enteros aleatorios entre 0 y 1,000,000.
    """
    return [random.randint(0, 1_000_000) for _ in range(size)]

# Tamaños de lista a probar
sizes = [100_000, 1_000_000, 10_000_000]

# Probar los algoritmos de ordenamiento
print("Comparación de algoritmos de ordenamiento:\n")
for size in sizes:
    print(f"--- Probando con tamaño de lista: {size} ---")
    random_list = generate_random_list(size)

    # Prueba con sorted() (Python integrado)
    print("Ordenando con `sorted()` (Python integrado)...")
    time_sorted = measure_execution_time(lambda lst: sorted(lst), random_list)
    print(f"Tiempo: {time_sorted:.4f} segundos")

    # Prueba con QuickSort
    print("Ordenando con QuickSort...")
    time_quicksort = measure_execution_time(lambda lst: quicksort(lst), random_list[:])  # Copia de la lista
    print(f"Tiempo: {time_quicksort:.4f} segundos")

    # Prueba con Bubble Sort (solo para tamaños pequeños)
    if size <= 100_000:  # Bubble Sort es demasiado lento para listas grandes
        print("Ordenando con Bubble Sort...")
        time_bubble = measure_execution_time(lambda lst: bubble_sort(lst), random_list[:])  # Copia de la lista
        print(f"Tiempo: {time_bubble:.4f} segundos")
    else:
        print("Bubble Sort omitido para tamaños grandes (ineficiente).")