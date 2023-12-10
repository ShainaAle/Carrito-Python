import tkinter as tk
from PIL import Image, ImageTk
import serial
import threading

def encender():
    ser.write("encender\n".encode())
    print("Comando enviado: encender")
    estado_label.config(text="Estado: prendido")

def apagar():
    ser.write("apagar\n".encode())
    print("Comando enviado: apagar")
    estado_label.config(text="Estado: apagado")

def set_velocidad(valor):
    valor_str = "Velocidad: " + str(valor) + "\n"  # Convierte el valor a una cadena
    ser.write(valor_str.encode())  # Envía el valor de velocidad como una cadena
    print(f"Velocidad ajustada a: {valor}")

def recibir_datos():
    while True:
        try:
            dato = ser.readline().decode().strip()  # Lee un dato del puerto serie
            print(f"Dato recibido desde Micro:bit: {dato}")
            
            # Actualiza la etiqueta con el valor del objeto si es un número o cualquier cadena no vacía
            if dato.isdigit() or dato:
                objeto = int(dato) if dato.isdigit() else None
                objeto_label.config(text=f"Objeto en: {objeto} cm" if objeto is not None else "Objeto en: N/A")

        except serial.SerialException as e:
            print(f"Error en la recepción de datos: {e}")
            break

def mover_derecha():
    ser.write("derecha\n".encode())
    print("Comando enviado: derecha")

def mover_izquierda():
    ser.write("izquierda\n".encode())
    print("Comando enviado: izquierda")

def mover_arriba():
    ser.write("arriba\n".encode())
    print("Comando enviado: arriba")

def mover_abajo():
    ser.write("abajo\n".encode())
    print("Comando enviado: abajo")

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

# Conectar a la Micro:bit a través del puerto serie (ajusta el puerto y la velocidad según corresponda)
ser = serial.Serial('COM5', 115200)

# Iniciar la recepción de datos desde la Micro:bit en un hilo separado
recepcion_datos_thread = threading.Thread(target=recibir_datos)
recepcion_datos_thread.daemon = True  # Terminar el hilo cuando se cierre la ventana
recepcion_datos_thread.start()

# Crear botones y la barra controladora de velocidad
boton_encender_todos = tk.Button(ventana, text="Encender", command=encender, bg="lightgreen", padx=20, pady=10)
boton_apagar_todos = tk.Button(ventana, text="Apagar", command=apagar, bg="lightcoral", padx=20, pady=10)
boton_encender_todos.pack(pady=10)
boton_apagar_todos.pack(pady=10)

volumen_scale = tk.Scale(ventana, from_=0, to=100, orient="horizontal", label="Velocidad", command=set_velocidad)
volumen_scale.pack(pady=10)

# Etiqueta para mostrar la posición del objeto
objeto_label = tk.Label(ventana, text="Objeto en: N/A")
objeto_label.pack(pady=10)

# Botones para las flechas en forma de cruzeta
frame_botones = tk.Frame(ventana, bg="white")
frame_botones.pack()

boton_arriba = tk.Button(frame_botones, text="^", command=mover_arriba, font=("Arial", 16), padx=20, pady=10)
boton_izquierda = tk.Button(frame_botones, text="<", command=mover_izquierda, font=("Arial", 16), padx=20, pady=10)
boton_derecha = tk.Button(frame_botones, text=">", command=mover_derecha, font=("Arial", 16), padx=20, pady=10)
boton_abajo = tk.Button(frame_botones, text="v", command=mover_abajo, font=("Arial", 16), padx=20, pady=10)

boton_arriba.grid(row=0, column=1)
boton_izquierda.grid(row=1, column=0)
boton_derecha.grid(row=1, column=2)
boton_abajo.grid(row=2, column=1)

# Iniciar el bucle principal
ventana.mainloop()