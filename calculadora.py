# ------------------------------
# Operaciones matemáticas
# ------------------------------
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

# ------------------------------
# Menú con gatos
# ------------------------------
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

# ------------------------------
# Función para pedir opción
# ------------------------------
def pedir_opcion():
    while True:
        try:
            opcion = int(input("Selecciona una opción: "))
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("Error: Debes elegir un número entre 1 y 6.")
        except ValueError:
            print("Error: Debes ingresar un número entero.")

# ------------------------------
# Función para pedir números
# ------------------------------
def pedir_numero(texto):
    while True:
        try:
            return float(input(texto))
        except ValueError:
            print("Error: Debes ingresar un número válido.")

# ------------------------------
# Función para ejecutar operación
# ------------------------------
def ejecutar_operacion(opcion, num1, num2):
    if opcion == 1:
        return suma(num1, num2)
    elif opcion == 2:
        return resta(num1, num2)
    elif opcion == 3:
        return multiplicacion(num1, num2)
    elif opcion == 4:
        return division(num1, num2)
    elif opcion == 5:
        return potencia(num1, num2)
    elif opcion == 6:
        return "Salir"

# ------------------------------
# Programa principal
# ------------------------------
while True:
    mostrar_menu()
    opcion = pedir_opcion()

    if opcion == 6:
        print("¡Hasta luego! Gracias por usar la calculadora 😺")
        break

    num1 = pedir_numero("Primer número: ")
    num2 = pedir_numero("Segundo número: ")

    resultado = ejecutar_operacion(opcion, num1, num2)
    print("Resultado:", resultado, "\n")
