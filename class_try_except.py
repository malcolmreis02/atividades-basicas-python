
from lib2to3.pytree import Base


lista = [1, 2, 3, 4]
try:
    divisao = 10 / 1
    numero = lista[2]
    x = numero
except ZeroDivisionError:
    print('Não é possível realizar uma divisão por zero')
except IndexError:
    print('Essa lista não possui esse índice')
except BaseException as ex:
    print('Erro desconhecido: {}'.format(ex))
else:
    print('Executa mais códigos quando não acontecem erros')
finally:
    print('Executa de qualquer jeito: com erro ou sem erro')

# é tipo um try-catch
# todo erro é filho do BaseException
# para erros aritmeticos: ArithmeticError