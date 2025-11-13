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

print("\n====== CALCULADORA BÁSICA ======")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

opcion = int(input("Selecciona una opción: "))
num1 = float(input("Primer número: "))
num2 = float(input("Segundo número: "))

if opcion == 1:
    print("Resultado:", suma(num1, num2))
elif opcion == 2:
    print("Resultado:", resta(num1, num2))
elif opcion == 3:
    print("Resultado:", multiplicacion(num1, num2))
elif opcion == 4:
    print("Resultado:", division(num1, num2))
else:
    print("Error: la opción ingresada no existe. Debes elegir entre 1 y 4.")

