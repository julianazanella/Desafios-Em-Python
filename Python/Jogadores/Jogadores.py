lista = []
lista1 = []
dados = {}
tot = 0
dados['nome'] = str(input('Digite o nome do jogador: '))
partidas = int(input('Quantas partidas o jogador jogou? '))
for g in range(0,partidas):
    gols = int(input(f'Quantos gols na partida {g}: '))
    lista1.append(gols)
    dados['gols'] = lista1
    tot=tot+gols
dados['total'] = tot
lista.append(dados)
print('-='*30)
print (lista)
print('-='*30)
print('O campo nome tem valor:', lista[0]['nome'])
print('O campo gols tem o valor', lista1)
print('O campo total tem o valor', lista[0]['total'])
print('-='*30)
print(f'O jogador', lista[0]['nome'],f'jogou {partidas} partidas.')
for c in range(0,partidas):
    print(f'Na partida {c} fez {lista1[c]} gols')