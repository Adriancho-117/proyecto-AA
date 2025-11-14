def busqueda_lineal(lista, valor, key=None):
    valor = valor.lower() if isinstance(valor, str) else valor

    for item in lista:
        dato = item[key].lower() if key and isinstance(item[key], str) else (item[key] if key else item)

        if dato == valor:
            return item

    return None


def busqueda_binaria(lista, valor, key=None):
    izquierda = 0
    derecha = len(lista) - 1

    valor = valor.lower() if isinstance(valor, str) else valor

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        actual = lista[medio]
        dato = actual[key].lower() if key and isinstance(actual[key], str) else (actual[key] if key else actual)

        if dato == valor:
            return actual
        elif dato < valor:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return None
