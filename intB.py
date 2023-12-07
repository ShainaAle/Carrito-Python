import tkinter as tk
from PIL import Image, ImageTk
import serial
import threading

def encender():
    enviar_comando("encender")
    print("Comando enviado: encender")
    estado_label.config(text="Estado: prendido")

def apagar():
    enviar_comando("apagar")
    print("Comando enviado: apagar")
    estado_label.config(text="Estado: apagado")

def set_Velocidad(valor):
    enviar_comando(f"velocidad {valor}")
    print(f"Velocidad ajustada a: {valor}")

def recibir_datos():
    while True:
        try:
            dato = ser.readline().decode().strip()
            print(f"Dato recibido desde Micro:bit: {dato}")
            objeto_label = objeto_label.config(text=f"Objeto en: {dato}")
        except serial.SerialException:
            break

def mover_derecha():
    enviar_comando("derecha")
    print("Comando enviado: derecha")

def mover_izquierda():
    enviar_comando("izquierda")
    print("Comando enviado: izquierda")

def mover_arriba():
    enviar_comando("arriba")
    print("Comando enviado: arriba")

def mover_abajo():
    enviar_comando("abajo")
    print("Comando enviado: abajo")

def enviar_comando(comando):
    comando += "\n"
    ser.write(comando.encode())

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

# Conectar a la Micro:bit a través de Bluetooth (ajusta la dirección Bluetooth según corresponda)
bd_addr = 'D0:3A:6B:F5:45:60'  # Reemplaza con la dirección Bluetooth de tu dispositivo
port = 1  # Puerto de servicio para SPP (Serial Port Profile)

ser = serial.Serial(bd_addr, port)

# Iniciar la recepción de datos desde la Micro:bit en un hilo separado
recepcion_datos_thread = threading.Thread(target=recibir_datos)
recepcion_datos_thread.daemon = True
recepcion_datos_thread.start()

# Iniciar el bucle principal
ventana.mainloop()
