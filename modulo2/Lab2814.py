#Laboratorio 2.8.1.4 Leer enteros de forma segura
#Elaborado por: Ariadna Loredo Estrada

def read_int(prompt, min, max):
    ok = False
    while not ok:
        try:
            valor = int(input(prompt))
            ok = True
        except ValueError:
            print("Error: entrada incorrecta")
        if ok:
            ok = valor >= min and valor <= max
        if not ok:
            print("Error: el valor no está dentro del rango permitido (" + str(min) + ".." + str(max) + ")")
    return valor;

v = read_int("Ingresa un numero entre -10 a 10: ", -10, 10)

print("El número es:", v)