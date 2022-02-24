# criando uma class

class Calculadora:
  def __init__(self, num1, num2):
    self.a = num1
    self.b = num2

  def som(self):
    return self.a + self.b

  def sub(self):
    return self.a - self.b

  def mul(self):
    return self.a * self.b

  def div(self):
    return self.a / self.b
  
num1 = int(input("Digite o primeiro número: "))
num2 = int(input('Digite o segundo número: '))

calculadora = Calculadora(num1, num2)

# acessando os parametros passados
## print("Primeiro parâmetro: {}".format(calculadora.b))
## print('Segundo parâmetro: {}\n'.format(calculadora.a))

# acessando as funções com os parametros dados acima
# só vai executar isso abaixo caso nao se trate de um import 
print(__name__)
if __name__ == '__main__':
    print('Soma: {}'.format(calculadora.som()))
    print('Subtração: {}'.format(calculadora.sub()))
    print('Multiplicação: {}'.format(calculadora.mul()))
    print('Divisão: {}'.format(calculadora.div()))