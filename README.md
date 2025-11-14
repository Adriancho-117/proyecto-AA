# proyecto-AA

Instrucciones rápidas para ejecutar los tests en Windows (PowerShell):

1. Crear un entorno virtual (recomendado):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Instalar dependencias:

```powershell
python -m pip install -r requirements.txt
```

3. Ejecutar todos los tests:

```powershell
python -m pytest -v
```

Notas:
- Si prefieres usar el comando `pytest` directo, asegúrate de activar el entorno virtual.
- `requirements.txt` contiene `pytest` para reproducibilidad.
