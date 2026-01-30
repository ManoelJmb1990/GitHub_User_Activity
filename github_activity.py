import sys
import json
import urllib.request





def main():
    # Verifica se o usuário informou o username
    if(len(sys.argv) < 2):
        print("Uso Correto:")
        print("python github_activity.py <usarname>")
        return

    username = sys.argv[1]

    # Monta a URL da API usando o username
    url = f"https://api.github.com/users/{username}/events"

    print("Buscando dados da URL:")
    print(url)
    print("-" * 40)

    try:
        # Faz a requisição HTTP
        with urllib.request.urlopen(url) as response:
            # Lê o conteúdo da resposta
            data = response.read()

            # Converte bytes → string → objeto Python
            events = json.loads(data.decode("utf-8"))

            #imprime o json cru
            print(events)

    except Exception as error:
        print("Erro ao acessar a API do GitHub")
        print(error)

# Garante que o main só roda quando o arquivo é executado diretamente
if __name__ == "__main__":
    main()

