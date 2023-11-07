import tkinter as tk
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

def set_Velocidad(valor):
    valor_str = str(valor)  # Convierte el valor a una cadena
    ser.write(valor_str.encode())  # Envía el valor de velocidad como una cadena
    print(f"Velocidad ajustada a: {valor}")

def recibir_datos():
    while True:
        try:
            dato = ser.readline().decode().strip()  # Lee un dato del puerto serie
            print(f"Dato recibido desde Micro:bit: {dato}\n")
        except serial.SerialException:
            break

# Crear la ventana
ventana = tk.Tk()
ventana.title("Control Micro:bit")
ventana.configure(bg="pink")
ventana.geometry("500x500")

# Crear etiqueta para mostrar el estado
estado_label = tk.Label(ventana, text="Estado: ")
estado_label.pack()

# Conectar a la Micro:bit a través del puerto serie (ajusta el puerto y la velocidad según corresponda)
ser = serial.Serial('COM5', 115200)

# Iniciar la recepción de datos desde la Micro:bit en un hilo separado
recepcion_datos_thread = threading.Thread(target=recibir_datos)
recepcion_datos_thread.daemon = True  # Terminar el hilo cuando se cierre la ventana
recepcion_datos_thread.start()

# Crear botones y la barra controladora de velocidad
boton_encender_todos = tk.Button(ventana, text="Encender", command=encender)
boton_apagar_todos = tk.Button(ventana, text="Apagar", command=apagar)
boton_encender_todos.pack(pady=10)
boton_apagar_todos.pack(pady=10)

volumen_scale = tk.Scale(ventana, from_=0, to=100, orient="horizontal", label="Velocidad", command=set_Velocidad)
volumen_scale.pack(pady=10)

# Colocar los botones en la ventana
boton_encender_todos.pack()
boton_apagar_todos.pack()

# Iniciar el bucle principal
ventana.mainloop()
