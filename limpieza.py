import pandas as pd
import re

# Cargar el archivo CSV
file_path = "carbono.csv"  # Cambia esto al nombre de tu archivo CSV
df = pd.read_csv(file_path)

# Función para limpiar y organizar las columnas
def limpiar_columna(val):
    if pd.isna(val):
        return val
    # Eliminar comillas simples y dobles
    val = val.replace("'", "").replace('"', '')
    # Separar elementos por comas y eliminar espacios adicionales
    val = ' '.join(val.split())
    # Reemplazar múltiples comas consecutivas con una sola coma
    val = re.sub(r',+', ',', val)
    # Asegurarse de que las comas estén seguidas por un espacio si no lo están
    val = ', '.join([x.strip() for x in val.split(',') if x.strip()])
    return val

# Aplicar la función a las columnas Cooking_With y Recycling
df['Cooking_With'] = df['Cooking_With'].apply(limpiar_columna)
df['Recycling'] = df['Recycling'].apply(limpiar_columna)

# Guardar el DataFrame modificado en un nuevo archivo CSV
output_file_path = "carbono.csv"
df.to_csv(output_file_path, index=False)

print(f"Limpieza completada. Archivo guardado como {output_file_path}.")
