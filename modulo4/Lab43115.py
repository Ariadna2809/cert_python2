#Laboratorio 4.3.1.15 Histograma de frecuencia de caracteres
#Elaborado por: Ariadna Loredo Estrada

from os import strerror

archivo = input('Introduce el nombre del archivo: ')
def histograma(archivo):
    dic = {}
    try:
        handler = open(archivo, mode = 'r')
        contenido = handler.readline().lower()
        for letra in contenido:
            dic[letra] =  contenido.count(letra)
        
        for k,v in sorted(dic.items()):
            print(k,'->',v)
        
    except FileNotFoundError:
        print('Archivo no encontrado:', archivo)
        exit()
        
histograma(archivo)