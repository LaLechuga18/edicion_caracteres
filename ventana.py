import tkinter as tk
from tkinter import filedialog
import pandas as pd

def seleccionar_archivo():
    archivo = filedialog.askopenfilename(filetypes=[("Archivos CSV", "*.csv")])
    if archivo:
        entry_ruta.delete(0, tk.END)
        entry_ruta.insert(0, archivo)

def combinar_secuencias():
    ruta_archivo = entry_ruta.get()
    if ruta_archivo:
        df = pd.read_csv(ruta_archivo)
        secuencia_adn = df['string_a_modificar'].iloc[0]
        secuencias_modificadas = []

        for _, row in df.iterrows():
            posicion = row['posicion']
            alteracion = row['alteracion']
            secuencia_adn = secuencia_adn[:posicion] + alteracion + secuencia_adn[posicion + 1:]

        resultado_combinacion.set(secuencia_adn)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Combinador de Secuencias")

# Crear y posicionar widgets
etiqueta_archivo = tk.Label(ventana, text="Archivo CSV:")
etiqueta_archivo.grid(row=0, column=0, padx=5, pady=5)

entry_ruta = tk.Entry(ventana, width=40)
entry_ruta.grid(row=0, column=1, padx=5, pady=5)

boton_seleccionar = tk.Button(ventana, text="Seleccionar Archivo", command=seleccionar_archivo)
boton_seleccionar.grid(row=0, column=2, padx=5, pady=5)

boton_combinar = tk.Button(ventana, text="Combinar Secuencias", command=combinar_secuencias)
boton_combinar.grid(row=1, column=1, padx=5, pady=5)

resultado_combinacion = tk.StringVar()
etiqueta_resultado = tk.Label(ventana, text="Resultado:")
etiqueta_resultado.grid(row=2, column=0, padx=5, pady=5)
label_resultado = tk.Label(ventana, textvariable=resultado_combinacion, wraplength=400)
label_resultado.grid(row=2, column=1, columnspan=2, padx=5, pady=5)

# Iniciar el bucle de eventos
ventana.mainloop()
