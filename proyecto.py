# proyecto-AA

# Desencriptador de clave usando ordenamiento por inserción
import ipywidgets as widgets
from IPython.display import display, clear_output

import time

def ordenar_insercion(clave):
    """Ordena una lista de números usando el algoritmo de inserción."""
    for i in range(1, len(clave)):
        actual = clave[i]
        j = i - 1
        while j >= 0 and clave[j] > actual:
            clave[j + 1] = clave[j]
            j -= 1
        clave[j + 1] = actual
    return clave


def desencriptar():
    print("Desencriptador de Clave Telefónica")
    texto = input("Ingresa la clave (números separados por espacios): ").strip()

    if not texto:
        print(" No ingresaste ningún número. Intenta nuevamente.")
        return

    try:
        clave_codificada = [int(x) for x in texto.split()]
    except ValueError:
        print("Error: ingresa solo números separados por espacios.")
        return

    inicio = time.time()
    clave_desencriptada = ordenar_insercion(clave_codificada.copy())
    fin = time.time()
    duracion = fin - inicio

    print(f"\nClave codificada: {clave_codificada}")
    print(f" Clave desencriptada: {''.join(map(str, clave_desencriptada))}")
    print(f" Tiempo de ejecución: {duracion:.6f} segundos")


if __name__ == "__main__":
    desencriptar()
