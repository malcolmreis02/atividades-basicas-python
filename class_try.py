# validando a entrada de um dado
# enquando ele nao digitar um numero, ele vai pedir pra inserir o dado novamente

class Error(Exception):
    pass
# para criar um erro personalizado é necessário que haja um erro como esse acima que nao faça nada

class InputError(Error):
    def __init__(self, message):
        self.message = (message)
# depois de criar um erro personalizado, na função você cria uma condição para que apareça tal erro, junto com a mensagem que você quer


while True:
    try:
        x = int(input('Entre com uma nota de 0 a 10: '))
        print(x)
        if x> 10 or x<0:
            raise InputError('Nota não pode ser maior que 10')
        break
    except ValueError:
        print('Valor inválido, digite apenas número')
    except InputError as ex:
        print(ex)