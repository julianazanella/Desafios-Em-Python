num3 = 0

while num3 != 5:
    num = int(input('DIGITE O PRIMEIRO NUMERO: '))
    num2 = int(input('DIGITE O SEGUNDO NUMERO: '))
    num3 = int(input("""DIGITE A OPERAÇÃO NO MENU: 
        [1] SOMAR
        [2] MULTIPLICAR 
        [3] MAIOR 
        [4] NOVOS NUMEROS
        [5] SAIR DO PROGRAMA """))
    if num3 == 1:
        print ('A SOMA DOS NUMEROS É: ',(num+num2))
    if num3 == 2:
        print('A MULTIPLICAÇÃO DOS NUMEROS É:',(num*num2))
    if num3 == 3:
        print('O MAIOR NUMERO ENTRE OS DIGITADOS É: ',(max(num,num2)))
    if num3 ==4:
        print('DIGITE NOVOS NUMEROS')
    if num3 ==5:
        print('FIM')
    if num3>5:
        print('NUMERO INVALIDO')




