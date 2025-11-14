from estudiantes import cargar_estudiantes
from ordenamiento import bubble_sort, insertion_sort, quicksort
from src.busqueda import busqueda_lineal, busqueda_binaria

def main():
    estudiantes = cargar_estudiantes()

    print("Estudiantes cargados:")
    print(estudiantes)

    print("\nOrdenados (Bubble):")
    print(bubble_sort(estudiantes, key="nombre"))

    print("\nBuscar 'Carlos':")
    print(busqueda_lineal(estudiantes, "Carlos", key="nombre"))

if __name__ == "__main__":
    main()
