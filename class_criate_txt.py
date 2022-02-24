def escrever_arquivo(texto):
    arquivo = open('criated.txt', 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(texto):
    arquivo = open('criated.txt', 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

if __name__ == '__main__':
#    escrever_arquivo('Essa e a minha primeira linha.\n')
#    atualizar_arquivo('Essa e a minha terceira linha.\n')
    ler_arquivo('criated.txt')