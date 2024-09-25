import os

def encontrar_arquivo_com_string(diretorio, string):
    # Lista para armazenar arquivos que contêm a string
    arquivos_encontrados = []
    
    # Percorre todos os arquivos na pasta
    for nome_arquivo in os.listdir(diretorio):
        # Verifica se o arquivo termina com .txt
        if nome_arquivo.endswith('.txt'):
            caminho_arquivo = os.path.join(diretorio, nome_arquivo)
            # Abre o arquivo e procura pela string
            with open(caminho_arquivo, 'r', encoding='utf-8') as file:
                conteudo = file.read()
                if string in conteudo:
                    arquivos_encontrados.append(nome_arquivo)

    return arquivos_encontrados

# Caminho da pasta que contém os arquivos .txt
diretorio = r"C:\Users\Cliente\Desktop\NCBI"
string_procurada = "AG099"

# Chama a função e armazena os resultados
resultados = encontrar_arquivo_com_string(diretorio, string_procurada)

# Imprime os nomes dos arquivos encontrados
if resultados:
    print("Arquivos que contêm a string '{}':".format(string_procurada))
    for arquivo in resultados:
        print(arquivo)
else:
    print("Nenhum arquivo encontrado com a string '{}'.".format(string_procurada))
