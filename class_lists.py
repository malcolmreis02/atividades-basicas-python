conjunto1 = {3, 4}
conjunto2 = {1, 2, 3, 4, 5}

conjunto_subset = conjunto1.issubset(conjunto2) 
print('O conjunto 1 é subconjunto do conjunto 2? {}'.format(conjunto_subset))
# confere se o conjunto 1 é um subconjunto do conjunto 2

conjunto_superconjunto = conjunto2.issuperset(conjunto1) 
print('O conjunto 2 é superconjunto do conjunto 1?: {}'.format(conjunto_superconjunto))
# confere se o conjunto 2 é superconjunto do conjunto 1 *superconjunto é quando o outro é seu subconjunto

# como o conjunto tira a duplicidade, você pode converter uma lista com possíveis itens repetidos para um conjunto e depois, se quiser, transformar ela em lista novamente
list1 = [1,2,2,3,4,5]
set_list1 = set(list1)
print('Essa é o conjunto sem duplicidade dessa lista: {}'.format(set_list1))
new_list1 = list(set_list1)
print('Essa é a lista atualizada sem duplicidade: {}'.format(new_list1))