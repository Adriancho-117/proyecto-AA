# proyecto-AA

# Desencriptador de clave usando ordenamiento por inserción
import ipywidgets as widgets
from IPython.display import display, clear_output

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

# --- Widgets ---
titulo = widgets.HTML("<h3>🔐 Desencriptador de Clave Telefónica</h3>")
entrada = widgets.Text(
    description="Clave:",
    placeholder="Ejemplo: 9 3 1 5 2",
    layout=widgets.Layout(width="50%")
)
boton = widgets.Button(description="Desencriptar", button_style="info")
salida = widgets.Output()

# --- Lógica al presionar el botón ---
def desencriptar(b):
    with salida:
        clear_output()
        texto = entrada.value.strip()
        if not texto:
            print("No ingresaste ningún número. Intenta nuevamente.")
            return
        try:
            clave_codificada = [int(x) for x in texto.split()]
        except ValueError:
            print(" Error: ingresa solo números separados por espacios.")
            return
        
        clave_desencriptada = ordenar_insercion(clave_codificada.copy())
        print(f"Clave codificada: {clave_codificada}")
        print(f"lave desencriptada: {''.join(map(str, clave_desencriptada))}")

boton.on_click(desencriptar)

# --- Mostrar todo ---
display(titulo, entrada, boton, salida)
