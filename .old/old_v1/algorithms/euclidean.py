#!/bin/python3

def eucl_alg(x, y):
    show_proc = []
    
    while y != 0:
        show_proc.append((x, y))
        x, y = y, x % y

    show_proc.append((x, y)) 
    
    print("Procedimiento completo:")
    for step in show_proc[:-1]:
        print(f"{step[0]} = ({step[1]})({step[0] // step[1]}) + {step[0] % step[1]}")

    print(f"\nMCD = {show_proc[-2][1]}")

while True:
    try:
        x = int(input("Ingrese el primer número (x): "))
        y = int(input("Ingrese el segundo número (y): "))
    except ValueError:
        print("Por favor, ingrese números enteros válidos.")
    else:
        eucl_alg(x, y)

    frwd = input("¿Quieres realizar otra prueba? (s/n): ").lower()
    if frwd != 's':
        break
