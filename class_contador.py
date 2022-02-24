from class_for_in import list_animal

contador_letras = lambda lista: [len(x) for x in lista]
print(sum(contador_letras(list_animal)))

# aqui importamos uma lista ja feita, fizemos uma função anonima que conta o tamanho (numero de letras) de cada palavra de 
# cada item de uma lista recebida e, após isso, retornamos o total de letras que essa lista possui