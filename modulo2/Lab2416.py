#Laboratorio 2.4.1.6 Un Display LED
#Elaborado por: Ariadna Loredo Estrada

digitos = ['1111110', 
    '0110000',
    '1101101',
    '1111001',
    '0110011',
    '1011011',
    '1011111',
    '1110000',
    '1111111',
    '1111011',
    ]
    
def print_numero(num):
    global digitos
    dig = str(num)
    led = ['' for lin in range(5)]
    for d in dig:
        seg = [[' ',' ',' '] for lin in range(5)]
        patron = digitos[ord(d)-ord('0')]
        if patron[0] == '1':
            seg[0][0] = seg[0][1] = seg[0][2] = '#'
        if patron[1] == '1':
            seg[0][2] = seg[1][2] = seg[2][2] = '#'
        if patron[2] == '1':
            seg[2][2] = seg[3][2] = seg[4][2] = '#'
        if patron[3] == '1':
            seg[4][0] = seg[4][1] = seg[4][2] = '#'
        if patron[4] == '1':
            seg[2][0] = seg[3][0] = seg[4][0] = '#'
        if patron[5] == '1':
            seg[0][0] = seg[1][0] = seg[2][0] = '#'
        if patron[6] == '1':
            seg[2][0] = seg[2][1] = seg[2][2] = '#'
        for lin in range(5):
            led[lin]+=''.join(seg[lin])+' '
    for lin in led:
        print(lin)
        
print_numero(int(input("Ingresa cualquier número entero no negativo: ")))