def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: No se puede dividir entre cero."
    return a / b

def potencia(a, b):
    return a ** b

def mostrar_menu():
    print("====================================")
    print("  (=^･ω･^=)  CALCULADORA  (=^･ω･^=)  ")
    print("      INGENIERIA DE SOFTWARE I       ")
    print("====================================")
    print(" 1. Suma      🐾")
    print(" 2. Resta     🐾")
    print(" 3. Multiplicación 🐾")
    print(" 4. División  🐾")
    print(" 5. Potencia  🐾")
    print(" 6. Salir     🐾")
    print("====================================")


# Validación para evitar letras u otros caracteres
try:
    opcion = int(input("Selecciona una opción: "))
except ValueError:
    print("Error: Debes ingresar un número válido.")
    exit()

try:
    num1 = float(input("Primer número: "))
    num2 = float(input("Segundo número: "))
except ValueError:
    print("Error: Solo puedes ingresar números.")
    exit()

if opcion == 1:
    print("Resultado:", suma(num1, num2))
elif opcion == 2:
    print("Resultado:", resta(num1, num2))
elif opcion == 3:
    print("Resultado:", multiplicacion(num1, num2))
elif opcion == 4:
    print("Resultado:", division(num1, num2))
elif opcion == 5:
    print("Resultado:", potencia(num1, num2))
else:
    print("Error: la opción ingresada no existe. Debe elegir entre 1 y 5.")
