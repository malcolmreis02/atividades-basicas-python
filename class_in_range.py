a = int(input('Digite um número para sabermos se ele é primo: '))
cont = 0

for b in range(1, a+1):
  resto = a % b
  if resto==0:
    cont=cont+1

if cont>2:
  print('O número não é primo')
else:
  print('O número é primo') 
