#Laboratorio 4.5.1.22 Los módulos datetime y time
#Elaborado por: Ariadna Loredo Estrada

from datetime import datetime

d = datetime(2020,11,4,14,53)
print(d.strftime("%Y/%m/%d %H:%M:%S"))
print(d.strftime("%y/%B/%d %H:%M:%S %p"))
print(d.strftime("%a, %Y %b %d"))
print(d.strftime("%A, %Y %B %d"))
print("Weekday:",d.strftime("%w"))
print("Day of the year:",d.strftime("%j"))
print("Week number fo the year:",d.strftime("%U"))