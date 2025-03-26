"""
Determina el mayor de tres números ingresados por el teclado
"""


def intercambiar_valores(numero1, numero2):
    return numero2, numero1  # Simplificación del intercambio


numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))
numero3 = int(input("Ingresa el tercer número: "))

if numero1 > numero2:
    numero1, numero2 = intercambiar_valores(numero1, numero2)

if numero2 > numero3:
    numero2, numero3 = intercambiar_valores(numero2, numero3)

if numero1 > numero2:
    numero1, numero2 = intercambiar_valores(numero1, numero2)

print(f"Números ordenados: {numero1}, {numero2}, {numero3}")
print(f"El mayor es {numero3}")
