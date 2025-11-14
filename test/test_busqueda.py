import pytest
from src.ordenamiento import bubble_sort, insertion_sort, quicksort

lista_simple = [5, 1, 9, 3]
lista_dict = [
    {"nombre": "Carlos", "promedio": 4.5},
    {"nombre": "Ana", "promedio": 4.8},
    {"nombre": "Luis", "promedio": 3.9}
]

def test_bubble_sort_simple():
    assert bubble_sort(lista_simple) == [1, 3, 5, 9]

def test_bubble_sort_dict():
    ordenado = bubble_sort(lista_dict, key="nombre")
    assert ordenado[0]["nombre"] == "Ana"
    assert ordenado[-1]["nombre"] == "Luis"

def test_insertion_sort_simple():
    assert insertion_sort(lista_simple) == [1, 3, 5, 9]

def test_quicksort_simple():
    assert quicksort(lista_simple) == [1, 3, 5, 9]
