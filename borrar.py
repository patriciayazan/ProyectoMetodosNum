import tkinter as tk
from tkinter import messagebox, Toplevel, ttk
import numpy as np
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr


class FunctivaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Functiva")
        self.root.geometry("600x600")
        self.root.configure(bg="lightblue")
        self.create_widgets()

    def create_widgets(self):
        # Título de la aplicación
        self.title_label = tk.Label(self.root, text="Functiva", font=("Helvetica", 24, "bold"), bg="lightblue")
        self.title_label.pack(pady=10)

        # Labels and Entries for function input
        self.func_label = tk.Label(self.root, text="Ingrese la función:", bg="lightblue")
        self.func_label.pack()

        self.func_entry = tk.Entry(self.root, width=50)
        self.func_entry.pack()

        self.func_button = tk.Button(self.root, text="Cargar Función", command=self.cargar_funcion, bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"))
        self.func_button.pack(pady=5)

        # Input para valores de a y b
        self.a_label = tk.Label(self.root, text="A:", bg="lightblue")
        self.a_label.pack()
        self.a_entry = tk.Entry(self.root, width=10)
        self.a_entry.pack()

        self.b_label = tk.Label(self.root, text="B:", bg="lightblue")
        self.b_label.pack()
        self.b_entry = tk.Entry(self.root, width=10)
        self.b_entry.pack()

        # Selección de tipo de método
        self.method_type_label = tk.Label(self.root, text="Seleccione el tipo de método:", bg="lightblue")
        self.method_type_label.pack()

        self.method_type_var = tk.StringVar(value="Métodos Abiertos")
        self.method_type_menu = tk.OptionMenu(self.root, self.method_type_var, "Métodos Abiertos", "Métodos Cerrados", command=self.update_method_menu)
        self.method_type_menu.pack()

        # Método específico
        self.method_label = tk.Label(self.root, text="Seleccione el método específico:", bg="lightblue")
        self.method_label.pack()

        self.method_var = tk.StringVar(value="Newton-Raphson")
        self.method_menu = tk.OptionMenu(self.root, self.method_var, "Newton-Raphson", "Secante")
        self.method_menu.pack()

        self.solve_func_button = tk.Button(self.root, text="Resolver Función", command=self.resolver_funcion, bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"))
        self.solve_func_button.pack(pady=5)

        self.integrate_button = tk.Button(self.root, text="Integrar Función", command=self.integrar_funcion, bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"))
        self.integrate_button.pack(pady=5)

        # Labels and Entries for matrix input

        #ttk.Separator(self.root, orient=tk.HORIZONTAL).place(relx=0, rely=0.76, relheight=1, relwidth=1) 
        
        #-----------------------------------------
        self.method_type_label = tk.Label(self.root, text="Seleccione el tipo de solución:", bg="lightblue")
        self.method_type_label.pack()

        self.matrix_method_var = tk.StringVar(value="Gauss")  # Define correctamente la variable
        self.method_type_menu = tk.OptionMenu(self.root, self.matrix_method_var, "Gauss", "Gauss-Jordan", "Matriz Inversa")

        self.method_type_menu.pack()

        #-----------------------------------------------------------
        self.matrix_label = tk.Label(self.root, text="Ingrese la matriz (separada por comas y líneas):", bg="lightblue")
        self.matrix_label.pack()

        self.matrix_text = tk.Text(self.root, height=5, width=50)
        self.matrix_text.pack()

        self.matrix_button = tk.Button(self.root, text="Cargar Matriz", command=self.cargar_matriz, bg="#2196F3", fg="white", font=("Helvetica", 12, "bold"))
        self.matrix_button.pack(pady=5)


        self.solve_button = tk.Button(self.root, text="Resolver Sistema de Ecuaciones", command=self.resolver_ecuaciones, bg="#2196F3", fg="white", font=("Helvetica", 12, "bold"))
        self.solve_button.pack(pady=5)

    def update_method_menu(self, selection):
        # Cambiar el menú de métodos según el tipo seleccionado
        if selection == "Métodos Abiertos":
            self.method_var.set("Newton-Raphson")
            self.method_menu['menu'].delete(0, 'end')
            self.method_menu['menu'].add_command(label="Newton-Raphson", command=tk._setit(self.method_var, "Newton-Raphson"))
            self.method_menu['menu'].add_command(label="Secante", command=tk._setit(self.method_var, "Secante"))
        elif selection == "Métodos Cerrados":
            self.method_var.set("Bisección")
            self.method_menu['menu'].delete(0, 'end')
            self.method_menu['menu'].add_command(label="Bisección", command=tk._setit(self.method_var, "Bisección"))
            self.method_menu['menu'].add_command(label="Falsa Posición", command=tk._setit(self.method_var, "Falsa Posición"))

    

    def cargar_funcion(self):
        funcion_str = self.func_entry.get()

        try:
            self.funcion = parse_expr(funcion_str)
            messagebox.showinfo("Éxito", f"Función cargada correctamente: {self.funcion}")
        except Exception as e:
            messagebox.showerror("Error", f"Error al cargar la función: {e}")

    def integrar_funcion(self):
        if hasattr(self, 'funcion'):
            try:
                x = sp.symbols('x')
                # Método de integración simbólica
                integral = sp.integrate(self.funcion, (x, 0, 1))
                self.show_result(f"Integral calculada: {integral}")
            except Exception as e:
                messagebox.showerror("Error", f"Error al integrar la función: {e}")
        else:
            messagebox.showerror("Error", "Primero cargue una función válida.")

    def cargar_matriz(self):
        matriz_str = self.matrix_text.get("1.0", tk.END).strip()
        try:
            matriz = [list(map(float, row.split(','))) for row in matriz_str.split('\n') if row]
            self.matriz = np.array(matriz)
            messagebox.showinfo("Éxito", f"Matriz cargada correctamente: \n{self.matriz}")
        except Exception as e:
            messagebox.showerror("Error", f"Error al cargar la matriz: {e}")
   
    def resolver_ecuaciones(self):
        if hasattr(self, 'matriz'):
            metodo = self.matrix_method_var.get()
            try:
                A = self.matriz[:, :-1]
                b = self.matriz[:, -1]
                
                if metodo == "Gauss-Jordan":
                    self.gauss_jordan(A, b)
                elif metodo == "Matriz Inversa":
                    self.matriz_inversa(A, b)
                elif metodo == "Gauss":
                    self.gauss(A, b)
            except np.linalg.LinAlgError as e:
                messagebox.showerror("Error", f"Error al resolver las ecuaciones: {e}")
        else:
            messagebox.showerror("Error", "Primero cargue una matriz válida.")

    def gauss(self, A, b):
        try:
            n = len(b)
            # Método de eliminación de Gauss
            for i in range(n):
                for j in range(i + 1, n):
                    ratio = A[j, i] / A[i, i]
                    A[j, :] -= ratio * A[i, :]
                    b[j] -= ratio * b[i]
            # Sustitución hacia atrás
            x = np.zeros(n)
            for i in range(n - 1, -1, -1):
                x[i] = (b[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]
            self.show_result(f"Solución por Gauss: \n{x}")
        except Exception as e:
            messagebox.showerror("Error", f"Error en Gauss: {e}")

    def gauss_jordan(self, A, b):
        try:
            # Crear la matriz aumentada
            augmented_matrix = np.hstack([A, b.reshape(-1, 1)])
            n = len(b)
            
            for i in range(n):
                # Verificar si el pivote es cero
                if augmented_matrix[i, i] == 0:
                    # Buscar una fila con un pivote no cero y hacer un intercambio
                    for k in range(i + 1, n):
                        if augmented_matrix[k, i] != 0:
                            augmented_matrix[[i, k]] = augmented_matrix[[k, i]]  # Intercambio de filas
                            break
                    else:
                        raise ValueError("El sistema no tiene solución única (pivote cero en Gauss-Jordan).")
                
                # Escalar la fila para que el pivote sea 1
                augmented_matrix[i] = augmented_matrix[i] / augmented_matrix[i, i]
                
                # Eliminar los elementos en la columna del pivote para otras filas
                for j in range(n):
                    if i != j:  # No modificar la fila actual
                        augmented_matrix[j] -= augmented_matrix[i] * augmented_matrix[j, i]
            
            # Extraer la solución de la última columna de la matriz aumentada
            solution = augmented_matrix[:, -1]
            self.show_result(f"Solución por Gauss-Jordan: \n{solution}")
        except Exception as e:
            messagebox.showerror("Error", f"Error en Gauss-Jordan: {e}")


    def matriz_inversa(self, A, b):
        try:
            inv_A = np.linalg.inv(A)
            solution = np.dot(inv_A, b)
            self.show_result(f"Solución por Matriz Inversa: \n{solution}")
        except np.linalg.LinAlgError as e:
            messagebox.showerror("Error", f"Error al calcular la matriz inversa: {e}")

    def resolver_funcion(self):
        metodo_principal = self.method_type_var.get()
        metodo_especifico = self.method_var.get()
        a = float(self.a_entry.get())
        b = float(self.b_entry.get())

        if hasattr(self, 'funcion'):
            x = sp.symbols('x')
            if metodo_principal == "Métodos Abiertos":
                if metodo_especifico == "Newton-Raphson":
                    self.newton_raphson(self.funcion, x)
                elif metodo_especifico == "Secante":
                    self.secante(self.funcion, x)
            elif metodo_principal == "Métodos Cerrados":
                if metodo_especifico == "Bisección":
                    self.biseccion(self.funcion, x, a, b)

                elif metodo_especifico == "Falsa Posición":
                    self.falsa_posicion(self.funcion, x, a ,b)
        else:
            messagebox.showerror("Error", "Primero cargue una función válida.")
    
    def newton_raphson(self, funcion, x):
        pass  # Implementa lógica de Newton-Raphson

    def secante(self, funcion, x):
        pass  # Implementa lógica de Secante

    def biseccion(self, funcion, x, a, b):
        pass  # Implementa lógica de Bisección

    def falsa_posicion(self, funcion, x, a, b):
        pass  # Implementa lógica de Falsa Posición

    def show_result(self, text):
        result_window = Toplevel(self.root)
        result_window.title("Resultado")
        result_label = tk.Label(result_window, text=text)
        result_label.pack(pady=10)

# Crear la ventana principal y ejecutar la app
if __name__ == "__main__":
    root = tk.Tk()
    app = FunctivaApp(root)
    root.mainloop()
