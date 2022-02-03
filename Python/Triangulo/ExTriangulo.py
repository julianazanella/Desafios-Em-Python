r1 = float(input('Informe o valor do primeiro segmento: '))
r2 = float(input('Informe o valor do segundo segmento: '))
r3 = float(input('Informe o valor do terceiro segmento:'))
if r1< (r2+r3) or r2< (r1+r3) or r3< (r1+r2):
    print('Os segmentos informados PODEM formar um triaangulo!!')
    if (r2==r3==r1):
        print('O triangulo é EQUILATERO')
    elif r1!=r2!=r3!=r1:
        print('O triangulo é ESCALENO!')
    else:
         print('O triangulo é ISOCELES')
else:
    print('Os segmentos informados NÃO PODEM formar um triangulo!!')
