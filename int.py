import tkinter as tk
import serial

def encender():
    ser.write("encender\n".encode())
    print("Comando enviado: encender")
    estado_label.config(text="Estado: prendido")

def apagar():
    ser.write("apagar\n".encode())
    print("Comando enviado: apagar")
    estado_label.config(text="Estado: apagado")


# Crear la ventana
ventana = tk.Tk()
ventana.title("Control Micro:bit")
ventana.configure(bg="pink")  # Establecer el fondo de ventana en color rosa
ventana.geometry("500x500")  # Establecer el tamaño de la ventana en 500x500 píxeles


# Crear etiqueta para mostrar el estado
estado_label = tk.Label(ventana, text="Estado: ")
estado_label.pack()

# Conectar a la Micro:bit a través del puerto serie (ajusta el puerto y la velocidad según corresponda)
ser = serial.Serial('COM5', 115200)  # Reemplaza 'COMX' con el nombre de tu puerto serie

# Crear botones
boton_encender_todos = tk.Button(ventana, text="Encender", command=encender)
boton_apagar_todos = tk.Button(ventana, text="Apagar", command=apagar)
boton_encender_todos.pack(pady=10)  # Agregar un espacio vertical de 10 píxeles entre los botones
boton_apagar_todos.pack(pady=10)     # Agregar un espacio vertical de 10 píxeles entre los botones

# Colocar los botones en la ventana
boton_encender_todos.pack()
boton_apagar_todos.pack()

# Iniciar el bucle principal
ventana.after(1000)
ventana.mainloop()
