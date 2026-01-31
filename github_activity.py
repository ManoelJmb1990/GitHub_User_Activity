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

            if not events:
                print("Nenhuma atividade pública encontrada para este usuário")
                return

            #imprime o json cru
            print("Atividades recentes:")
            print("-" * 40)
            for event in events:
                event_type = event["type"]
                repo_name = event["repo"]["name"]

                if event_type == "PushEvent":
                    commits = event["payload"]["commit"]
                    quantidade = len(commits)
                    print(f"Enviou {quantidade} commits para {repo_name}")

                elif event_type == "WatchEvent":
                    print(f"Deu star em {repo_name}")

                elif event_type == "IssuesEvent":
                    print(f"Abríu uma issue em {repo_name}")

                else:
                    # Evento que não estamos tratando ainda
                    print(f"Realizou {event_type} em {repo_name}")

    except urllib.error.HTTPError as error:
        if error.code == 404:
            print("Usuário não encontrado no GitHub")
        else:
            print("Erro HTTP ao acessar a API do GitHub.")
            print("Código:", error.code)

    except Exception as error:
        print("Erro inesperado ao executar o programa.")
        print(error)

# Garante que o main só roda quando o arquivo é executado diretamente
if __name__ == "__main__":
    main()

