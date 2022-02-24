list_animal = ['dog', 'cat', 'monkey', 'elephant']
for x in list_animal:
  print(x)

tupla = (1, 2, 3, 4, 5, 6)
print('Tupla original: {}'.format(tupla))
# essa tupla é imutavel, não se adiciona e nem se elimina nenhum item

lenght = len(tupla)
print('Quantos itens tem essa tupla? {}'.format(lenght))
# aqui é para voce saber o tamanho da tupla ou da lista

new_list = list(tupla)
print('Nova lista feita do conteúdo da tupla: {}'.format(new_list))
# aqui converte a tupla em lista 

new_tuple = tuple(list_animal)
print('Nova tupla feita do conteúdo da lista: {}'.format(new_tuple))
# aqui converte a lista em tupla