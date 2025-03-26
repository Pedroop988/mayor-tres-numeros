'''
Deter,ina el mayor de tres numeros ingresados por el teclado
'''

numero1 = int(input("Ingrse el primer numero : "))
numero2 = int(input("Ingrse el segundo numero : "))
numero3 = int(input("Ingrse el tercer numero : "))

if numero1>numero2:
    temporal=numero1
    numero1=numero2
    numero2=temporal

if numero2>numero3:
    temporal=numero2
    numero2=numero3
    numero3=temporal

if numero1>numero2:
    temporal=numero1
    numero1=numero2
    numero2=temporal

print(f"numeros ordenados: {numero1},{numero2},{numero3}")
print(f"El mayor es {numero3}")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
