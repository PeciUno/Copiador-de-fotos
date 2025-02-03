import os
import shutil
import sys

# Carpeta donde está el ejecutable o script
if getattr(sys, 'frozen', False):
    script_dir = os.path.dirname(sys.executable)
else:
    script_dir = os.path.dirname(os.path.abspath(__file__))

# Solicitar el nombre del archivo de texto y carpetas
archivo_texto = input("Introduce el nombre del archivo de texto (con extensión): ")
origen = input("Introduce el nombre de la carpeta de origen de los archivos: ")
destino = input("Introduce el nombre de la carpeta de destino: ")

# Convertir a rutas absolutas
origen = os.path.join(script_dir, origen)
archivo_texto = os.path.join(script_dir, archivo_texto)
destino = os.path.join(script_dir, destino)

# Crear la carpeta de destino si no existe
if not os.path.exists(destino):
    os.makedirs(destino, exist_ok=True)
    print(f"Se ha creado la carpeta {destino}.")
else:
    print(f"La carpeta {destino} ya existía.")

# Verificar si el archivo de texto existe
if not os.path.exists(archivo_texto):
    print(f"No se ha encontrado el archivo de texto: {archivo_texto}")
    sys.exit()

# Verificar si la carpeta de origen existe
if not os.path.exists(origen):
    print(f"No se ha encontrado la carpeta de origen: {origen}")
    sys.exit()

# Leer el archivo de texto y obtener los números de las fotos
with open(archivo_texto, 'r') as file:
    fotos = [line.strip() for line in file if line.strip()]

copiados_jpg = 0
copiados_nef = 0
no_copiados = []

# Recorrer las fotos y copiarlas a la carpeta de destino
for foto in fotos:
    # Rellenar con ceros a la izquierda para formar 4 dígitos
    foto_formateada = foto.zfill(4)
    
    # Posibles nombres de archivo (con o sin guion bajo al principio)
    archivo_jpg_1 = f'DSC_{foto_formateada}.JPG'
    archivo_nef_1 = f'DSC_{foto_formateada}.NEF'
    archivo_jpg_2 = f'_DSC{foto_formateada}.JPG'
    archivo_nef_2 = f'_DSC{foto_formateada}.NEF'

    archivo_origen_jpg_1 = os.path.join(origen, archivo_jpg_1)
    archivo_origen_nef_1 = os.path.join(origen, archivo_nef_1)
    archivo_origen_jpg_2 = os.path.join(origen, archivo_jpg_2)
    archivo_origen_nef_2 = os.path.join(origen, archivo_nef_2)
    
    # Copiar archivos si existen
    copiado = False
    if os.path.exists(archivo_origen_jpg_1):
        shutil.copy2(archivo_origen_jpg_1, destino)
        copiados_jpg += 1
        copiado = True
        print(f"Copiado: {archivo_jpg_1}")
        
    if os.path.exists(archivo_origen_nef_1):
        shutil.copy2(archivo_origen_nef_1, destino)
        copiados_nef += 1
        copiado = True
        print(f"Copiado: {archivo_nef_1}")

    if os.path.exists(archivo_origen_jpg_2):
        shutil.copy2(archivo_origen_jpg_2, destino)
        copiados_jpg += 1
        copiado = True
        print(f"Copiado: {archivo_jpg_2}")

    if os.path.exists(archivo_origen_nef_2):
        shutil.copy2(archivo_origen_nef_2, destino)
        copiados_nef += 1
        copiado = True
        print(f"Copiado: {archivo_nef_2}")
    
    # Añadir a la lista de no copiados si ninguno se copió
    if not copiado:
        no_copiados.append(foto)

print(f"Se han copiado {copiados_jpg} fotos .jpg.")
print(f"Se han copiado {copiados_nef} fotos .nef.")

# Mostrar archivos no copiados si los hay
if no_copiados:
    print("No se han copiado los siguientes archivos:")
    for archivo in no_copiados:
        print(f'DSC_{archivo.zfill(4)}.JPG y DSC_{archivo.zfill(4)}.NEF')
