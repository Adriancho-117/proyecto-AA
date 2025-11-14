import json
import os

def cargar_estudiantes():
    # Obtener la ruta del directorio del proyecto
    ruta_proyecto = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ruta_archivo = os.path.join(ruta_proyecto, "Data", "estudiantes.json")
    
    with open(ruta_archivo, "r", encoding="utf-8") as f:
        return json.load(f)
