frase = input('Digite uma frase para analise: ').strip().upper()
frase1 = frase.replace(' ', '')
frase2 = frase1 [: : -1]

if frase1 == frase2:
    print('A FRASE É UM PALINDROMO!!')
else:
    print('A FRASE NÃO É UM PALINDROMO!!!')

print (frase1, frase2)