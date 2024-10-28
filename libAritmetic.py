from sympy import symbols, sympify


class Interprete:
    def interpretar_ecuacion(self, ecuacion):
        # Definir la variable
        x = symbols('x')

        # Convertir el string a una expresión matemática
        try:
            formula = sympify(ecuacion)
            return formula
        except Exception as e:
            return f"Error al interpretar la ecuación: {e}"

    def evaluar_ecuacion(self, ecuacion, valor):
        # Interpretar la ecuación
        formula = self.interpretar_ecuacion(ecuacion)

        # Definir la variable
        x = symbols('x')

        # Evaluar la expresión con el valor proporcionado
        resultado = formula.subs(x, valor)
        return resultado


inter = Interprete()

# Definir la ecuación como un string
ecuacion = "3*x**2 - 2"

# Interpretar la ecuación
formula = inter.interpretar_ecuacion(ecuacion)
print(f"Ecuación interpretada: {formula}")

# Evaluar la ecuación para un valor específico, por ejemplo, x = 2
valor = 2
resultado = inter.evaluar_ecuacion(ecuacion, valor)
print(f"El resultado de la ecuación para x={valor} es: {resultado}")

import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageTk
import sympy as sp

def mostrar_ecuacion(ecuacion):
    x = sp.symbols('x')
    try:
        formula = sp.sympify(ecuacion)
        ecuacion_latex = sp.latex(formula)

        # Generar la imagen de la ecuación en LaTeX
        fig, ax = plt.subplots()
        ax.text(0.5, 0.5, f"${ecuacion_latex}$", fontsize=20, ha='center')
        ax.axis('off')  # No mostrar ejes
        plt.savefig('ecuacion.png', bbox_inches='tight', pad_inches=0.1)
        plt.close(fig)

        # Cargar la imagen y mostrarla en Tkinter
        imagen = Image.open('ecuacion.png')
        imagen = imagen.resize((300, 100), Image.ANTIALIAS)
        return ImageTk.PhotoImage(imagen)

    except Exception as e:
        messagebox.showerror("Error", str(e))
        return None

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Conversor de Ecuaciones a LaTeX")

# Cuadro de texto para la entrada de la ecuación
entrada_ecuacion = tk.Entry(ventana, width=30)
entrada_ecuacion.pack(pady=10)

# Botón para mostrar la ecuación
def mostrar():
    ecuacion = entrada_ecuacion.get()
    imagen = mostrar_ecuacion(ecuacion)
    if imagen:
        label_imagen.config(image=imagen)
        label_imagen.image = imagen  # Mantener una referencia a la imagen

boton_mostrar = tk.Button(ventana, text="Mostrar en LaTeX", command=mostrar)
boton_mostrar.pack(pady=10)

# Label para mostrar la imagen
label_imagen = tk.Label(ventana)
label_imagen.pack(pady=10)

# Ejecutar la ventana
ventana.mainloop()
