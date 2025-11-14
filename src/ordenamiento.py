def bubble_sort(lista, key=None):
    arr = lista.copy()
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            a = arr[j][key] if key else arr[j]
            b = arr[j + 1][key] if key else arr[j + 1]

            if a > b:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def insertion_sort(lista, key=None):
    arr = lista.copy()

    for i in range(1, len(arr)):
        actual = arr[i]
        j = i - 1

        while j >= 0:
            a = arr[j][key] if key else arr[j]
            b = actual[key] if key else actual
            if a > b:
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break
        arr[j + 1] = actual

    return arr


def quicksort(lista, key=None):
    if len(lista) <= 1:
        return lista

    pivot = lista[len(lista) // 2]
    pivot_val = pivot[key] if key else pivot

    menores = [x for x in lista if (x[key] if key else x) < pivot_val]
    iguales = [x for x in lista if (x[key] if key else x) == pivot_val]
    mayores = [x for x in lista if (x[key] if key else x) > pivot_val]

    return quicksort(menores, key) + iguales + quicksort(mayores, key)
