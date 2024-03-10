#!/bin/python3

import sys

# Aqui estoy declarando varianles, si no, daria error al momento de revisarlas y no existan
og_x = 0
og_y = 0
education = False


# Aqui hago que si no se puso ningun argumento no haya problema
try:
    argumento = int(sys.argv[1])
except IndexError:
    pass


# Esta parte es de declaracion de variables en funcion del argumento
# esto es para poder hacer el video mas rapido y facil 
try:
    if argumento == 1:
        og_x = 527
        og_y = 1258
    elif argumento == 3:
        og_x = 163961
        og_y = 167181
    elif argumento == 0:
        education = True
        og_x = 527
        og_y = 1258
    else:
        pass
except NameError:
    pass


# Esto hace que si el primer valor del algoritmo euclideano fuera 0, lo elimina
def cero_del(array):
    if array and array[0] == 0:
        del array[0]
    return array

# Le agrega dos 0 al arreglo de cocinetes para poder resolverlo despues
def add_ceros(array):
    array.insert(0, 0)
    array.insert(0, 0)
    return array



# Esta es la funcion del algoritmo euclideando en si
def eucl_alg(x, y):
    show_proc = [] # Arreglo para luego mostrar el procedimiento
    cocientes = [] # Arreglo para guardar los cocientes 


# Este bucle es para ir haciendo las operaciones en si 
    while y != 0:
        show_proc.append((x, y))
        cociente = x // y
        cocientes.append(cociente)  
        x, y = y, x % y

    show_proc.append((x, y))

    print("\nMCD por algoritmo euclideano:\n")
    for step in show_proc[:-1]:
        print(f"{step[0]} = ({step[1]})({step[0] // step[1]}) + {step[0] % step[1]}")

    print(f"\nMaximo comun divisor = {show_proc[-2][1]}\n")
    mcd = show_proc[-2][1]

    return mcd, cocientes  # Retornamos el mcd y los cocientes 


# Esta es la funcion para sacar los valores de los arreglos x y y
# es decir, aqui estamos haciendo la tabla

def calcular_tabla(cocientes, x_arr, y_arr):

    for i in range(2, len(cocientes)):
        nuevo_x = cocientes[i] * x_arr[i - 1]  + x_arr[i - 2]
        nuevo_y = cocientes[i] * y_arr[i - 1]+ y_arr[i - 2]
        x_arr.append(nuevo_x)
        y_arr.append(nuevo_y)


while True:
    try:
        if og_x == 0:
            og_x = int(input("Ingrese el primer número (x): "))
            og_y = int(input("Ingrese el segundo número (y): "))

    except ValueError:
        print("Por favor, ingrese números enteros válidos.")

    else:
        mcd, cocientes = eucl_alg(og_x, og_y)  # Obtener el MCD y los cocientes
        break
    break

# Esta ahora si es la parte en donde ya empezamos a calcular la ecuacion en si 

# Sacando los nuevos valores de x y y
nw_x = (og_x / mcd)
nw_y = (og_y / mcd)

# Arreglo tantito el arreglo de coscientes 
cocientes = cero_del(cocientes)
cocientes = add_ceros(cocientes)

# Sacamos el valor de T
T = (len(cocientes) - 2)

# Creando los arreglos de x y y
x_arr = [0, 1]
y_arr = [1, 0]

if education == True:
    print(cocientes)
    print(x_arr)
    print(y_arr)
    input()
    

# Ahora si saco la tabla
calcular_tabla(cocientes, x_arr, y_arr)

# Y la imprimo 
print("Tabla resuelta: ")
print("Cocientes:", cocientes)
print("x_arr:    ", x_arr)
print("y_arr:    ", y_arr)

if education == True:
    input()
    print("\nCalculando las respuestas de x y y:")
    print("T = " + str(T) + "\n")
    print("x = " + "-1**" + str(T) + " * " + str(y_arr[T]))
    print("y = " + "-1**" + str(T + 1) + " * " + str(x_arr[T]))
    input()

# Ahora si sacamos las respuestas
x_respuesta = (( (-1) ** T) * y_arr[T])
y_respuesta = (( (-1) ** (T + 1)) * x_arr[T])

# Imprimimos las respuestas 
print("\nLa respuesta de X:", x_respuesta)
print("La respuesta de Y:", y_respuesta)
print(" ")

# Verificando el resultado 
if education == True:
    input()
    print( "(" + str(x_arr[-1]) + ")(" + str(x_respuesta) + ") + " + "(" + str(y_arr[-1]) + ")(" + str(y_respuesta) + ") = 1")
    input()
    print("(" + str(x_arr[-1] * x_respuesta) + ") + (" + str(y_arr[-1] * y_respuesta) + ") = 1")

