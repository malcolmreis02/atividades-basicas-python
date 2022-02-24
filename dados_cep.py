import pip._vendor.requests as requests

def Dados_cep():

    while True:
        cep = str(input('Digite somente os números do seu cep sem espaços nem pontos: '))
        response = requests.get('http://viacep.com.br/ws/{}/json'.format(cep))
        if response.status_code==200:
            try: 
                dic_cep = response.json()
                print('\nOpções:\n1-nome da rua\n2-bairro\n3-cidade\n4-ddd do local\n')
                number = int((input('\nDigite sua opção (apenas o número): ')))
                while (number<1) or (number>4):
                    if number<1 or number>4:
                        print("\nVocê não digitou uma opção válida")
                        print('\nOpções:\n1-nome da rua\n2-bairro\n3-cidade\n4-ddd do local\n')
                        number = int((input('\nDigite sua opção (apenas o número): ')))
            except BaseException as ex:
                print(ex)
            else:
                def Option(num):
                    if num == 1: 
                        return 'logradouro' 
                    elif num == 2: 
                        return 'bairro'
                    elif num ==3: 
                        return 'localidade'
                    elif num ==4: 
                        return 'ddd'

                real_option = Option(number)
                dado_pedido=dic_cep[real_option]
                print(dado_pedido)
                break
        else:
            print('Você não digitou um cep válido')

print(Dados_cep())