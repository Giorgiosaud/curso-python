import os
os.system("clear")
frutas=['manzana','pera','uva','fresa','kiwi']
for fruta in frutas:
    print(fruta)

cadena ="jorge"
for caracter in cadena:
    print(caracter)

#enumerate
# es una función que devuelve un objeto enumerado.
for index,fruta in enumerate(frutas):
    print(f"La fruta en la posición {index} es {fruta}")

#range
# es una función que devuelve una secuencia de números.
for numero in range(5):
    print(numero)

#bucles anidados
# Un bucle anidado es un bucle dentro de otro bucle.
# El bucle interno se ejecuta completamente cada vez que el bucle externo se ejecuta una vez.
for i in range(3):
    for j in range(3):
        print(f"i={i}, j={j}")

#break
# La instrucción break se utiliza para salir de un bucle.
animales=['perro','gato','pez','pájaro','tortuga']
for animal in animales:
    print(animal)
    if animal=='pez':
        break

#continue
# La instrucción continue se utiliza para saltar a la siguiente iteración de un bucle.
# En lugar de salir del bucle, como lo hace la instrucción break, la instrucción continue salta a la siguiente iteración del bucle.
for animal in animales:
    if animal=='pez':
        continue
    print(animal)

# list comprehension 
# Es una forma concisa de crear listas.
# Se pueden utilizar bucles for y condicionales en las listas de comprensión.
# Sintaxis:
# [expresión for elemento in iterable if condición]
# Ejemplo:
animales=['perro','gato','pez','pájaro','tortuga']
animales_en_mayusculas=[animal.upper() for animal in animales]
animales_primera_letra_mayuscula=[animal.capitalize() for animal in animales]
print(animales_en_mayusculas)
print(animales_primera_letra_mayuscula)
# como hago multiline elements es decir varias ejecuciones split mas otra cosa en comprensión de listas
# Ejemplo:
lista = [i for i in range(10) if i%2==0]
print(lista)
# Ejercicio 1: Lista de cuadrados
# Crea una lista de los cuadrados de los números del 1 al 10.
# Utiliza una lista de comprensión.
# diferencia range y array
# range es un generador de números
# array es una lista de números
# Ejemplo:
cuadrados=[i**2 for i in range(1,11)]
print(cuadrados)
# Ejercicio 2: Lista de pares
# Crea una lista de los números pares del 1 al 20.
# Utiliza una lista de comprensión.
# Ejemplo:
pares=[i for i in range(1,21) if i%2==0]
print(pares)

###
# EJERCICIOS (range)
###

# Ejercicio 1: Imprimir números del 1 al 10
# Imprime los números del 1 al 10 (inclusive) usando un bucle for y range().
print("\nEjercicio 1:")
for i in range(0,10):
    print(i+1)
# Ejercicio 2: Imprimir números impares del 1 al 20
# Imprime todos los números impares entre 1 y 20 (inclusive) usando un bucle for y range().
print("\nEjercicio 2:")
for i in range(1,20,2):
    print(i+1)
# Ejercicio 3: Imprimir múltiplos de 5
# Imprime los múltiplos de 5 desde 5 hasta 50 (inclusive) usando un bucle for y range().
print("\nEjercicio 3:")
for i in range(5,51,5):
    print(i)
# Ejercicio 4: Imprimir números en orden inverso
# Imprime los números del 10 al 1 (inclusive) en orden inverso usando un bucle for y range().
print("\nEjercicio 4:")
for i in range(10,0,-1):
    print(i)
# Ejercicio 5: Suma de números en un rango
# Calcula la suma de los números del 1 al 100 (inclusive) usando un bucle for y range().
print("\nEjercicio 5:")
suma=0
for i in range(1,101):
    suma+=i
print(suma)
# Ejercicio 6: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle for y range().
print("\nEjercicio 6:")
numero=int(input("Introduce un número: "))
for i in range(1,11):
    print(f"{numero} x {i} = {numero*i}")