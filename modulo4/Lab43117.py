#Laboratorio 4.3.1.17 Evaluando los resultados de los estudiantes
#Elaborado por: Ariadna Loredo Estrada

class StudentsDataException(Exception):
    pass


class WrongLine(StudentsDataException):
    def __init__(self, message):
        StudentsDataException.__init__(self)
        print(message)
        exit()


class FileEmpty(StudentsDataException):
    def __init__(self, message):
        StudentsDataException.__init__(self)
        print(message)
        exit()


