import tkinter as tk
from tkinter import ttk 
from ttkthemes import ThemedTk
    
    
    #3)Funcion para la calculadora de porcentaje
def calcular_porcentaje():
    try:
        cantidad = float(entry_cantidad.get())
        porcentaje = float(entry_porcentaje.get())
        resultado = (porcentaje / 100) * cantidad
        resultado_porcentaje.set(f"Resultado: {resultado: .2f}")
    except ValueError:
       resultado_porcentaje.set(text="Por favor ingresa números válidos.")


# Configuración de la ventana principal
window = ThemedTk(theme="adapta")
window.title=("Evidencias")
window.geometry("+500+800")

#Pestaña  Calculadora de porcentaje

ttk.Label(window,text="Cantidad").pack(padx=1, pady=5)
entry_cantidad= ttk.Entry(window)
entry_cantidad.pack(pady=5)

ttk.Label(window, text="Porcentaje (%)").pack(pady=5)
entry_porcentaje = ttk.Entry(window)
entry_porcentaje.pack(pady=5)


#BOTON
boton_calcular= ttk.Button(window, text="Calcular Porcentaje", command=calcular_porcentaje).pack(pady=5)

#RESULTADO
resultado_porcentaje= tk.StringVar()
ttk.Label(window, text= "Resultado: ").pack(pady=6)
ttk.Label(window, textvariable=resultado_porcentaje).pack(pady=5)



window.mainloop()