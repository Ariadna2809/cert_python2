#Laboratorio 4.3.1.17 Evaluando los resultados de los estudiantes
#Elaborado por: Ariadna Loredo Estrada

class StudentsDataException(Exception):
    pass

class WrongLine(StudentsDataException):
    def __init__(self, line_number, line_string):
        super().__init__(self)
        self.line_number = line_number
        self.line_string = line_string
class FileEmpty(StudentsDataException):
    def __init__(self):
        super().__init__(self)

from os import strerror
datos = { }
archivo = input("Introduce el nombre del archivo: ")
line_number = 1
try:
    f = open(archivo, "rt")
    lines = f.readlines()
    f.close()
    if len(lines) == 0:
        raise FileEmpty()
    for i in range(len(lines)):
        line = lines[i]
        columns = line.split()
        if len(columns) != 3:
            raise WrongLine(i + 1, line)
        student = columns[0] + ' ' + columns[1]
        try:
            points = float(columns[2])
        except ValueError:
            raise WrongLine(i + 1, line)
        try:
            datos[student] += points
        except KeyError:
            datos[student] = points
    # Imprimiendo resultados.
    for student in sorted(datos.keys()):
        print(student,'\t', datos[student])
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))
except WrongLine as e:
    print("Línea incorrecta #" + str(e.line_number) + " en el archivo fuente:" + e.line_string)
except FileEmpty:
    print("Archivo fuente vacío")


