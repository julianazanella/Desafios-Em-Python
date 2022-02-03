lista = []
print( '==========CADASTRO CLIENTE==========')

while True:
    doc = int(input('Digite o documento: '))
    if doc not in lista:
        lista.append(doc)
        print ('Documento cadastrado com sucesso!')
        nome = str(input('Digite o nome completo: ')).upper().strip()
        cont = str(input('Deseja encerrar o sistema? [S/N]')).upper().strip()
        while not cont in "SsnN":
            print('Opção invalida! Tente novamente')
            cont = str(input('Deseja encerrar o sistema? [S/N]')).upper().strip()
    else:
        print('Cliente já cadastrado no sistema')
        cont1 = str(input('Deseja encerrar o sistema? [S/N]')).upper().strip()
        if cont1 in 'Ss':
            break
print (lista)
