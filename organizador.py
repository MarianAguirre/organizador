import os
import pathlib
import shutil
from typing import List

SIN_EXTENSION = 'sin_extension'


def archivos_actuales(carpeta: str) -> List[str]:
    return [entry.name for entry in os.scandir(carpeta) if entry.is_file()] 
  
def archivosActualesRuta(carpeta: str) -> List[str]:
    return [entry.path for entry in os.scandir(carpeta) if entry.is_file()]

def contarArchivos (carpeta: str) ->int:
  return len(archivos_actuales(carpeta))

def extensiones(carpeta: str) -> List[str]:
  extensiones = {
    pathlib.Path(nombre).suffix or SIN_EXTENSION
    for nombre in archivos_actuales(carpeta)
  }
  return sorted(extensiones)

def crear_carpetas_por_extension(carpeta: str, extensiones: List[str]):
  for extension in extensiones:
    os.makedirs(os.path.join(carpeta, extension.replace('.', '')), exist_ok=True)


def copiar_archivos_a_carpetas(carpeta: str):
    for nombre in archivos_actuales(carpeta):
        ext = pathlib.Path(nombre).suffix or SIN_EXTENSION
        origen = os.path.join(carpeta, nombre)
        destino = os.path.join(carpeta, ext).replace('.', '')
        print(f"Copiando {nombre} a {ext}/")
        shutil.copy(origen, destino)
  
def eliminar_archivos(carpeta: str):
  for nombre in archivos_actuales(carpeta):
        print(f"Eliminando {nombre}")
        os.remove(nombre)
  


def main():
  carpetaActual:str = os.getcwd()
  extension = extensiones(carpetaActual)
  print(f'En tu carpeta actual existen {contarArchivos(carpetaActual)} archivos')
  print(f'Con las extensiones de {','.join(extension)}')
  
  crear = input('¿Crear carpetas para estos archivos? (si/no): ').strip().lower()
  if crear == 'si':
        print('Creando carpetas...')
        crear_carpetas_por_extension(carpetaActual, extension)
  if crear == 'no':
    print('Fin del programa')
    return

  copiar = input('¿Copiar los archivos a las carpetas correspondientes? (si/no): ').strip().lower()
  if copiar == 'si':
        print('Copiando archivos...')
        copiar_archivos_a_carpetas(carpetaActual)
  if copiar == 'no':
    print('Fin del programa')
    return
  
  eliminar = input('¿Eliminar los archivos originales? (si/no): ').strip().lower()
  if eliminar == 'si':
        eliminar_archivos(carpetaActual)
  if eliminar == 'no':
    print('Fin del programa')
    return


if __name__ == "__main__":
    main()