import tkinter as tk
from PIL import Image, ImageTk
import asyncio
import threading
import bleak

async def encender():
    await client.write_gatt_char(0x0011, bytearray([1]))
    print("Comando enviado: encender")
    estado_label.config(text="Estado: prendido")

async def apagar():
    await client.write_gatt_char(0x0011, bytearray([0]))
    print("Comando enviado: apagar")
    estado_label.config(text="Estado: apagado")

async def set_Velocidad(valor):
    valor_str = str(valor) + "\n"
    await client.write_gatt_char(0x0012, valor_str.encode())
    print(f"Velocidad ajustada a: {valor}")

async def recibir_datos():
    while True:
        try:
            dato = await client.read_gatt_char(0x0013)
            dato = dato.decode().strip()
            print(f"Dato recibido desde Micro:bit: {dato}")

            objeto_label.config(text=f"Objeto en: {dato}")

        except bleak.BleakError:
            break

async def mover_derecha():
    await client.write_gatt_char(0x0014, bytearray([1]))
    print("Comando enviado: derecha")

async def mover_izquierda():
    await client.write_gatt_char(0x0014, bytearray([2]))
    print("Comando enviado: izquierda")

async def mover_arriba():
    await client.write_gatt_char(0x0014, bytearray([3]))
    print("Comando enviado: arriba")

async def mover_abajo():
    await client.write_gatt_char(0x0014, bytearray([4]))
    print("Comando enviado: abajo")

async def conectar_ble(address, system_id):
    async with bleak.BleakClient(address, device=system_id) as client:
        await asyncio.gather(
            recibir_datos(),
            encender(),
            apagar(),
            mover_derecha(),
            mover_izquierda(),
            mover_arriba(),
            mover_abajo()
        )

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

# Dirección MAC de tu micro:bit
device_address = "D0:3A:6B:F5:45:60"

# System device ID relacionado con BluetoothLE
device_system_id = "BluetoothLE#BluetoothLEe0:2b:e9:aa:d3:b7-d0:3a:6b:f5:45:60"

# Conectar al dispositivo BLE en un hilo separado
conectar_thread = threading.Thread(target=lambda: asyncio.run(conectar_ble(device_address, device_system_id)))
conectar_thread.start()

# Crear botones y la barra controladora de velocidad
boton_encender_todos = tk.Button(ventana, text="Encender", command=encender, bg="lightgreen", padx=20, pady=10)
boton_apagar_todos = tk.Button(ventana, text="Apagar", command=apagar, bg="lightcoral", padx=20, pady=10)
boton_encender_todos.pack(pady=10)
boton_apagar_todos.pack(pady=10)

volumen_scale = tk.Scale(ventana, from_=0, to=100, orient="horizontal", label="Velocidad", command=set_Velocidad)
volumen_scale.pack(pady=10)

# Etiqueta para mostrar la posición del objeto
objeto_label = tk.Label(ventana, text="Objeto en: ")
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