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
    print("Se ha creado la carpeta.")
else:
    print("La carpeta ya existía.")

# Verificar si el archivo de texto existe
if not os.path.exists(archivo_texto):
    print("No se ha encontrado el archivo de texto.")
    sys.exit()

# Verificar si la carpeta de origen existe
if not os.path.exists(origen):
    print("No se ha encontrado la carpeta de origen.")
    sys.exit()

# Leer el archivo de texto y obtener los números de las fotos
with open(archivo_texto, 'r') as file:
    fotos = [line.strip() for line in file if line.strip()]

copiados_jpg = 0
copiados_nef = 0
no_copiados = []

# Recorrer las fotos y copiarlas a la carpeta de destino
for foto in fotos:
    archivo_jpg = f'DSC_0{foto}.JPG'
    archivo_nef = f'DSC_0{foto}.NEF'
    archivo_origen_jpg = os.path.join(origen, archivo_jpg)
    archivo_origen_nef = os.path.join(origen, archivo_nef)
    
    # Copiar archivos si existen
    copiado = False
    if os.path.exists(archivo_origen_jpg):
        shutil.copy(archivo_origen_jpg, destino)
        copiados_jpg += 1
        copiado = True
        
    if os.path.exists(archivo_origen_nef):
        shutil.copy(archivo_origen_nef, destino)
        copiados_nef += 1
        copiado = True
    
    # Añadir a la lista de no copiados si ninguno se copió
    if not copiado:
        no_copiados.append(foto)

print(f"Se han copiado {copiados_jpg} fotos .jpg.")
print(f"Se han copiado {copiados_nef} fotos .nef.")

# Mostrar archivos no copiados si los hay
if no_copiados:
    print("No se han copiado los siguientes archivos:")
    for archivo in no_copiados:
        print(f'DSC_0{archivo}.JPG y DSC_0{archivo}.NEF')

