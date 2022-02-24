# definindo uma funções
def som(a,b):
  return a+b

def sub(a,b):
  return a-b

def mul(a,b):
  return a*b

def div(a,b):
  return a/b

a = int(input('Digite um número: '))
b = int(input("Digite outro número: "))

print(' Soma: {}\n'.format(som(a,b)), 'Subtração: {}\n'.format(sub(a,b)), 'Multiplicação: {}\n'.format(mul(a,b)), 'Divisão: {}\n'.format(div(a,b)))