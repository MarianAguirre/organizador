import os
import pathlib
import shutil

carpetaActual:str = os.getcwd()


def archivosActuales():
  archivos: list = []
  with os.scandir(carpetaActual) as entries:
    for entry in entries:
      if entry.is_file():
        archivos.append(entry.name)
    return archivos
  
def archivosActualesRuta():
  archivos: list = []
  with os.scandir(carpetaActual) as entries:
    for entry in entries:
      if entry.is_file():
        archivos.append(entry.path)
    return archivos
  
def rutasActuales():
  rutas: list = []
  with os.scandir(carpetaActual) as entries:
    for entry in entries:
      if entry.is_dir():
        rutas.append(entry.path)
    return rutas

def contarArchivos ():
  count = archivosActuales()
  return len(count)
  
def extensiones():
  archivos = archivosActuales()
  extensiones = []
  for nombre in archivos:
    archivo_path = pathlib.Path(nombre)
    ext = archivo_path.suffix or 'sin_extension'
    extensiones.append(ext)
  return list(set(extensiones))




print(f'En tu carpeta actual existen {contarArchivos()} archivos')
print(f'Con las extensiones de {','.join(extensiones())}')
print('¿Crear carpetas para estos archivos?')
yesOrNot = input()
if(yesOrNot == 'si'):
  print('Creando las carpetas')
  for nombre in extensiones():
    nombreCarpeta = nombre
    path = os.path.join(carpetaActual, nombreCarpeta) 
    os.makedirs(path, exist_ok=True)
print ('¿Copiamos los archivos a las carpetas correspondientes?')
yesOrNot = input()
if(yesOrNot == 'si'):
  for nombre in archivosActuales():
        archivo_path = pathlib.Path(nombre)
        extension = archivo_path.suffix or 'sin_extension'
        origen = os.path.join(carpetaActual, nombre)
        print(origen)
        destino = os.path.join(carpetaActual, extension)
        print(destino)
        print(f"Moviendo {nombre} a {extension}/")
        shutil.copy(origen, destino)