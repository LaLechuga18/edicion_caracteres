import pandas as pd
import os

# Verificar si ya existe un archivo con el nombre base
nombre_base = "Combinaciones"
extension = ".csv"
contador = 1
nombre_archivo = f"{nombre_base}_{contador}{extension}"
while os.path.exists(nombre_archivo):
    contador += 1
    nombre_archivo = f"{nombre_base}_{contador}{extension}"

# Paso 1: Importar el archivo CSV
df = pd.read_csv("dataset.csv")

# Paso 2: Obtener la secuencia de ADN desde el archivo CSV
secuencia_adn = df['string_a_modificar'].iloc[0]

# Paso 3: Crear una lista para almacenar los datos modificados
secuencias_modificadas = []
secuencia_completa_modificada = secuencia_adn  # Inicializar la secuencia completa modificada

# Paso 4: Iterar sobre cada fila del DataFrame
for index, row in df.iterrows():
    posicion = row['posicion']
    alteracion = row['alteracion']
    secuencia_modificada = secuencia_adn[:posicion] + alteracion + secuencia_adn[posicion + 1:]
    secuencias_modificadas.append(f"{posicion},{alteracion},{secuencia_modificada}")
    # Actualizar la secuencia completa modificada
    secuencia_completa_modificada = secuencia_completa_modificada[:posicion] + alteracion + secuencia_completa_modificada[posicion + 1:]

# Paso 5: Guardar las secuencias modificadas en un nuevo archivo CSV
with open(nombre_archivo, "w") as f:
    f.write("posicion,alteracion,secuencia_modificada\n")
    for linea in secuencias_modificadas:
        f.write(linea + "\n")
    f.write(f"String modificado\n{secuencia_completa_modificada}\n")

print(f"Archivo guardado como: {nombre_archivo}")
