import math
print('==========SEJA BEM VINDO!!==========')
while True:
    saque = int(input('DIGITE O VALOR DO SAQUE: '))
    valor50 = (saque/50)
    if saque>=50:
        print('NOTAS DE R$50: ',math.floor(valor50))
        saque - ((math.floor(valor50))*50)
    dif = saque - ((math.floor(valor50)) * 50)
    if dif>=20:
        dif10 = dif - (math.floor(dif / 20) * 20)
        print ('NOTAS DE R$20:', math.floor(dif/20))
        if dif10<=10:
            print('NOTAS DE R$1: ', dif - (math.floor(dif/20)*20))
        if dif10>10:
            print('NOTAS DE R$10:', math.floor(dif10/10))
            print('NOTAS DE R$1:', (dif10-(math.floor(dif10/10)*10)))
    if dif<20:
        print('NOTAS DE R$10:', math.floor(dif/10))
        print('NOTAS DE R$1:', (dif - (math.floor(dif/10)*10)))
    cont = ' '
    while cont not in 'nNsS':
        cont = str(input('DESEJA CONTINUAR?')).upper().strip()
    if cont == 'N':
        break
print ('OPERAÇÃO FINALIZADA')
print('==========OBRIGADA POR USAR NOSSOS SERVIÇOS==========')


