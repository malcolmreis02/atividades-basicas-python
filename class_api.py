import pip._vendor.requests as requests

# pedindo para o usuário digitar seu cep para saber o nome da rua 
cep = str(input('Digite somente os números do seu cep seme eespaços nem pontos: '))

# fazendo o chamado da api
response = requests.get('http://viacep.com.br/ws/{}/json'.format(cep))

# vendo se é sucesso o pedido que foi feito
print('\nstatus code: {}'.format(response.status_code))

# observando o conteúdo json que a api trouxe
print('\ncontend: {}\n'.format(response.text))

# transformando o que veio da api (json) em um dicionário
dados_cep = response.json()
print('\ntransforming json in a object:\n{}'.format(dados_cep))

# pedindo um determinado dado da informação que a api trouxe
nome_rua = dados_cep['logradouro']
print('\nnome da rua que cujo cep foi pedido: {}\n'.format(nome_rua))





