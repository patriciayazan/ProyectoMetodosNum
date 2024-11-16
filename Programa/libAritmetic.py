from sympy import symbols, sympify, sqrt


class Interprete:
    @staticmethod
    def interpretar_ecuacion(ecuac):
        # Definir la variable
        x = symbols('x')

        # Convertir el string a una expresión matemática
        try:
            form = sympify(ecuac)
            return form
        except Exception as e:
            return f"Error al interpretar la ecuación: {e}"

    def evaluar_ecuacion(self, ecuac, val):
        # Interpretar la ecuación
        form = self.interpretar_ecuacion(ecuac)

        # Definir la variable
        x = symbols('x')

        # Evaluar la expresión con el valor proporcionado, devolviendo un valor decimal
        result = form.subs(x, val).evalf()
        return result


inter = Interprete()

# # Definir la ecuación como un string
# ecuacion = "3 * sqrt(x) - 2"
#
# # Interpretar la ecuación
# formula = inter.interpretar_ecuacion(ecuacion)
# print(f"Ecuación interpretada: {formula}")
#
# # Evaluar la ecuación para un valor específico, por ejemplo, x = 2
# valor = 2
# resultado = inter.evaluar_ecuacion(ecuacion, valor)
# print(f"El resultado de la ecuación para x={valor} es: {resultado}")

