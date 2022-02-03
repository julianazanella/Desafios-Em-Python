from random import randint
lista=[]
def sorteio():
    lista.clear()
    for c in range(0,5):
        num = randint(1,10)
        lista.append(num)
    print(f'Os numeros sorteados foram: {lista}')

def pares():
    soma = 0
    for p in lista:
        if p%2==0:
            soma = soma+p
    print(f'Somando os valores pares da lista {lista}, temos o valor: {soma}')
    print('='*30)

sorteio()
pares()

sorteio()
pares()