# proyecto-AA

# Desencriptador de clave usando ordenamiento por inserción

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

if __name__ == "__main__":
    print(" Desencriptador de clave telefónica\n"
    # Solicitar clave desde la terminal
    entrada = input("Ingresa tu clave desordenada")

  # Convertir la entrada en lista de enteros
   try:
        clave_codificada = [int(x) for x in entrada.split()]
    except ValueError:
        print(" Error: Asegúrate de ingresar solo números separados por espacios.")
        exit()

  if not clave_codificada:
        print(" No ingresaste ningún número. Intenta nuevamente.")
        exit()

   print(f"\nClave codificada: {clave_codificada}")

   # Desencriptar clave
   
clave_desencriptada = ordenar_insercion(clave_codificada.copy())
    # Mostrar resultado
    print(f"Clave desencriptada: {''.join(map(str, clave_desencriptada))}")
