import tkinter as tk
from PIL import Image, ImageTk
import pygatt
import gatt
import threading

def encender():
    enviar_comando("encender")
    print("Comando enviado: encender")
    estado_label.config(text="Estado: prendido")

# Agrega el resto de las funciones como apagar, set_velocidad, etc.

def recibir_datos(device, characteristic):
    while True:
        try:
            dato = characteristic.read_value().decode().strip()
            print(f"Dato recibido desde Micro:bit: {dato}")
            objeto_label.config(text=f"Objeto en: {dato}")
        except (gatt.exceptions.NotConnectedError, UnicodeDecodeError):
            break

def enviar_comando(comando):
    comando += "\n"
    ser.char_write(CHARACTERISTIC_UUID, bytearray(comando, 'utf-8'))

# Crear la ventana
ventana = tk.Tk()
ventana.title("Control Micro:bit")

# Configurar la imagen de fondo
ruta_imagen = "C:/Users/shain/OneDrive/Escritorio/Escuela/Programables-P/Carrito-Python/fondo.jpg"
imagen_fondo = Image.open(ruta_imagen)
imagen_fondo = ImageTk.PhotoImage(imagen_fondo)
fondo_label = tk.Label(ventana, image=imagen_fondo)
fondo_label.place(relwidth=1, relheight=1)

# Crear etiqueta para mostrar el estado
estado_label = tk.Label(ventana, text="Estado: ", bg="white")
estado_label.pack(pady=10)

# Especificar la dirección Bluetooth de tu dispositivo Micro:bit
bd_addr = 'D0:3A:6B:F5:45:60'  # Reemplaza con la dirección Bluetooth de tu dispositivo

# UUID del servicio y la característica en la micro:bit
SERVICE_UUID = "6e400001-b5a3-f393-e0a9-e50e24dcca9e"
CHARACTERISTIC_UUID = "6e400003-b5a3-f393-e0a9-e50e24dcca9e"

# Conectar a la Micro:bit a través de Bluetooth (ajusta la dirección Bluetooth según corresponda)
puerto_serial = "COM5"
ser = pygatt.GATTToolBackend()
ser.start()
device = ser.connect(bd_addr)

# Configurar la característica para lectura/escritura
characteristic = None

# Iniciar la recepción de datos desde la Micro:bit en un hilo separado
recepcion_datos_thread = threading.Thread(target=recibir_datos, args=(device, characteristic))
recepcion_datos_thread.daemon = True
recepcion_datos_thread.start()

# Resto del código...

# Iniciar el bucle principal
ventana.mainloop()

