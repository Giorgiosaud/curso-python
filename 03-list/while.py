import os
os.system("clear")
iterador=0
while iterador<6:
    if iterador==3:
        print("Iterador es igual a 3")
        iterador+=1
        continue
    print(iterador)
    iterador+=1
    print("Iterador incrementado",iterador)
# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.
print("\nEjercicio 1:")
numero = 10
while numero > 0:
    print(numero)
    numero -= 1
# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
print("\nEjercicio 2:")
numero = 1
suma = 0
while numero<=20:
    if numero%2==0:
        suma+=numero
    numero+=1
print(f"La suma de los números pares entre 1 y 20 es: {suma}")
# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
print("\nEjercicio 3:")
factorial=1
try:
    numero=int(input("Introduce un número entero positivo: "))
    if numero<0:
        raise Exception("El número introducido no es un número entero positivo")
except:
    print("El valor introducido no es un número entero positivo")
    exit()
while numero>=1:
    factorial*=numero
    numero -= 1
print(f"El factorial del número es: {factorial}")
# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".
print("\nEjercicio 4:")
contraseña=''
while len(contraseña)<8:
    contraseña= input("Introduce una contraseña: ")
    if len(contraseña)<8:
        print("La contraseña debe tener al menos 8 caracteres")
print("Contraseña válida")

# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
print("\nEjercicio 5:")
tabla=int(input("Introduce un número para la tabla: "))
multiplicador=1
while multiplicador<=10:
    print(f"{tabla} x {multiplicador} = {tabla*multiplicador}")
    multiplicador+=1
# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.
print("\nEjercicio 6:")
divisor=2
is_prime=True
try:
    numero=int(input("Introduce un número entero positivo: "))
    if numero<0:
        raise Exception("El número introducido no es un número entero positivo")
except:
    print("El valor introducido no es un número entero positivo")
    exit()
while divisor<=numero:
    is_prime=True
    for i in range(2,divisor):
        if divisor%i==0:
            is_prime=False
            break
    if is_prime:
        print(f"el numero{divisor} es primo")
    divisor+=1