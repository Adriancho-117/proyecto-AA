import pytest
from src.estudiantes import cargar_estudiantes

def test_cargar_estudiantes():
    estudiantes = cargar_estudiantes()
    assert isinstance(estudiantes, list)
    assert len(estudiantes) > 0
    assert "nombre" in estudiantes[0]
    assert "promedio" in estudiantes[0]