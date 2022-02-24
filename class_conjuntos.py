conjunto = {1, 2, 3, 4 ,5}
# conjunto.add(6) -> função que adiciona um objeto no conjunto
# conjunto.discart(2) -> função que remove um objeto no conjunto

conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6, 7, 8, 9, 10}

conjunto_uniao = conjunto1.union(conjunto2) 
print('Fazendo uma união e retirando a duplicidade: {}'.format(conjunto_uniao))
# função que junta as uniões e tiram a duplicidade

conjunto_interseccao = conjunto1.intersection(conjunto2)
print('Fazendo uma intersecção: {}'.format(conjunto_interseccao)) 
# função que faz a intersecção dos conjuntos

conjunto_diferenca = conjunto1.difference(conjunto2) 
print('Vendo o que o conjunto 1 tem de diferente do conjunto 2: {}'.format(conjunto_diferenca))
# função que faz aparecer os numeros que tem no 1 e que nao tem no 2

conjunto_dif_simetrica = conjunto1.symmetric_difference(conjunto2) 
print('Vendo o que os conjuntos têm de diferentes entre si: {}'.format(conjunto_dif_simetrica))
# função que faz aparecer o numeros que só tem no 1 e numeros que so tem no 2