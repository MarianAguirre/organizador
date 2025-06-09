# 🗂️ Organizador de Archivos en Python

Este es un organizador de archivos escrito en Python, capaz de clasificar archivos por extensión y organizarlos en carpetas. Cuenta con **dos versiones** disponibles:

- 📁 Versión de **terminal**
- 🖥️ Versión con **interfaz gráfica (GUI)** utilizando PyQt6

---

## 🚀 Características

- Detecta archivos en la carpeta actual
- Clasifica archivos por su extensión
- Crea carpetas automáticamente para cada tipo de archivo
- Copia archivos a las carpetas correspondientes
- Elimina archivos originales si el usuario lo desea
- Interfaz gráfica simple y clara (GUI)
- Funciona en sistemas Windows, Linux y macOS

---

## 📦 Requisitos

- Python 3.10 o superior
- PyQt6 (solo para la versión GUI)

Instalación de dependencias:

```bash
pip install PyQt6
```

# 📁 Versión de Terminal
## ▶️ Ejecución

```bash
python organizador_terminal.py
```

## 💬 Ejemplo de uso

En tu carpeta actual existen 15 archivos
Con las extensiones de .txt,.jpg,.png
¿Crear carpetas para estos archivos? (si/no): si
Creando carpetas...
¿Copiar los archivos a las carpetas correspondientes? (si/no): si
Copiando archivos...
¿Eliminar los archivos originales? (si/no): no
Fin del programa

Esta versión permite organizar archivos desde la consola de forma interactiva. Muy útil para automatizaciones o uso rápido sin interfaz.

# 🖥️ Versión con Interfaz Gráfica (GUI)
## ▶️ Ejecución

```bash
python organizador.py
```

## 🧭 Flujo de la aplicación

    Muestra la cantidad de archivos y sus extensiones.

    Pregunta si deseas crear carpetas por tipo de archivo.

    Opción para copiar archivos a las carpetas creadas.

    Opción final para eliminar los archivos originales.

    Finaliza automáticamente tras unos segundos.

## 📂 Estructura del Proyecto

organizador_gui.py        # Interfaz gráfica con PyQt6
organizador_terminal.py   # Versión por terminal
README.md                 # Este archivo
