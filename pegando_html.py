from urllib import request
import pip._vendor.requests as requests

def Retorna_html():
    url = str(input("Coloque aqui o link da página cuja você deseja o html: "))
    response = requests.get(url)
    print(response.text)

if __name__ == '__main__':
    Retorna_html()