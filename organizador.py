import os
import pathlib
import shutil
from typing import List
from PyQt6.QtCore import QSize, Qt, pyqtSignal, pyqtSlot, QTimer
from PyQt6.QtWidgets import QApplication, QPushButton, QMainWindow, QLabel, QVBoxLayout, QWidget
import sys

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
  


class primeraVentana(QWidget):
  cambio_a_segunda = pyqtSignal()
  cambio_a_fin = pyqtSignal()
  
  def __init__(self):
        super().__init__()
        carpetaActual:str = os.getcwd()
        extension = extensiones(carpetaActual)
        label1 = QLabel(f"En tu carpeta actual existen {contarArchivos(carpetaActual)} archivos")
        label2 = QLabel(f"Con las extensiones de {', '.join(extension)}")
        label3 = QLabel("¿Crear carpetas para estos archivos?")
        buttonSi = QPushButton("Si")
        buttonNo = QPushButton("No")
        
        font = label1.font()
        font.setPointSize(16)
        for lbl in (label1, label2, label3):
            lbl.setFont(font)
            lbl.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        
        layout = QVBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)
        layout.addWidget(buttonSi)
        layout.addWidget(buttonNo)
        
        buttonSi.clicked.connect(self.cambio_a_segunda.emit)
        buttonNo.clicked.connect(self.cambio_a_fin.emit)
        
        buttonSi.clicked.connect(lambda:crear_carpetas_por_extension(carpetaActual, extension))

        self.setLayout(layout)

class segundaVentana(QWidget):
  cambio_a_fin = pyqtSignal()
  cambio_a_tercera =pyqtSignal()
  
  def __init__(self):
        carpetaActual:str = os.getcwd()
        super().__init__()
        label1 = QLabel(f"Creando carpetas...")
        label2 = QLabel(f"¿Copiar los archivos a las carpetas correspondientes?")
        buttonSi = QPushButton("Si")
        buttonNo = QPushButton("No")
        
        font = label1.font()
        font.setPointSize(16)

        for lbl in (label1, label2):
          lbl.setFont(font)
          lbl.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        
        layout = QVBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(label2)
    
        layout.addWidget(buttonSi)
        layout.addWidget(buttonNo)
        
        buttonNo.clicked.connect(self.cambio_a_fin.emit)
        buttonSi.clicked.connect(self.cambio_a_tercera.emit)
        
        buttonSi.clicked.connect(lambda:copiar_archivos_a_carpetas(carpetaActual))
        

        self.setLayout(layout)

class terceraVentana(QWidget):
  cambio_a_fin = pyqtSignal()
  cambio_a_cuarta = pyqtSignal()
  
  def __init__(self):
        carpetaActual:str = os.getcwd()

        super().__init__()
        label1 = QLabel(f"Copiando archivos...")
        label2 = QLabel(f"¿Eliminar los archivos originales?")
        
        buttonSi = QPushButton("Si")
        buttonNo = QPushButton("No")
        
        font = label1.font()
        font.setPointSize(16)

        for lbl in (label1, label2):
          lbl.setFont(font)
          lbl.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        
        layout = QVBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(label2)
        

        layout.addWidget(buttonSi)
        layout.addWidget(buttonNo)
        
        buttonNo.clicked.connect(self.cambio_a_fin.emit)
        buttonSi.clicked.connect(self.cambio_a_cuarta.emit)
        
        buttonSi.clicked.connect(lambda:eliminar_archivos(carpetaActual))
        

        self.setLayout(layout)
        
class cuartaVentana(QWidget):
  def __init__(self):
        super().__init__()
        label1 = QLabel(f"Eliminando archivos...")
        label2 = QLabel(f"La ventana se auto cerrara en 3 segundos")
        
        font = label1.font()
        font.setPointSize(16)

        for lbl in (label1, label2):
          lbl.setFont(font)
          lbl.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        
        layout = QVBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(label2)

        self.setLayout(layout)

class finPrograma(QWidget):
  def __init__(self):
    super().__init__()
    labelFin = QLabel("FIN DEL PROGRAMA")
    label2 = QLabel(f"La ventana se auto cerrara en 3 segundos")
    font = labelFin.font()
    font2 = label2.font()
    font.setPointSize(30)
    font2.setPointSize(15)
    labelFin.setFont(font)
    label2.setFont(font2)
    for lbl in (label2, labelFin):
      lbl.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
    layout = QVBoxLayout()
    layout.addWidget(labelFin)
    layout.addWidget(label2)
    self.setLayout(layout)

class main(QMainWindow):
  def __init__(self):
        super().__init__()
        self.setWindowTitle("El  organizainador")
        self.dialogo1 = primeraVentana()
        self.dialogo2 = segundaVentana()
        self.dialogo3 = terceraVentana()
        self.dialogo4 = cuartaVentana()
        
        
        self.finPrograma = finPrograma()
        
        self.setCentralWidget(self.dialogo1)
        self.setFixedSize(QSize(750, 300))

        # ✅ Conectar señal para cambiar de pantalla
        self.dialogo1.cambio_a_segunda.connect(self.mostrar_dialogo2)
        self.dialogo2.cambio_a_tercera.connect(self.mostrar_dialogo3)
        self.dialogo3.cambio_a_cuarta.connect(self.mostrar_dialogo4)
        
        self.dialogo1.cambio_a_fin.connect(self.mostrar_fin)
        self.dialogo2.cambio_a_fin.connect(self.mostrar_fin)
        self.dialogo3.cambio_a_fin.connect(self.mostrar_fin)
        
        
  @pyqtSlot()
  def cerrar_ventana(self):
        self.timer = QTimer(self)
        self.timer.setSingleShot(True)  
        self.timer.timeout.connect(self.close)  
        self.timer.start(3000)

  def closeEvent(self, event):
        if hasattr(self, 'timer') and self.timer.isActive():
            self.timer.stop()
        super().closeEvent(event)
  def mostrar_dialogo2(self):
    self.setCentralWidget(self.dialogo2)
  def mostrar_dialogo3(self):
    self.setCentralWidget(self.dialogo3)
  def mostrar_dialogo4(self):
    self.setCentralWidget(self.dialogo4)
    self.cerrar_ventana()
  def mostrar_fin(self):
    self.setCentralWidget(self.finPrograma)
    self.cerrar_ventana()

app = QApplication(sys.argv)

window = main()
window.show()  
app.exec()
