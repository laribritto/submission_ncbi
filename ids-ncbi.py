import os
import csv

def atualizar_headers(csv_arquivo, pasta_ncb):
    # Lê os IDs e nomes dos arquivos do CSV
    ids_nomes = {}
    with open(csv_arquivo, 'r') as csvfile:
        leitor = csv.reader(csvfile)
        next(leitor)  # Pular o cabeçalho
        for linha in leitor:
            if len(linha) == 2:
                sequence_id, nome_arquivo = linha
                ids_nomes[nome_arquivo] = sequence_id
    
    # Atualiza os headers dos arquivos na pasta NCBI
    for nome_arquivo in os.listdir(pasta_ncb):
        if nome_arquivo.endswith('.txt'):  # Alterar para .txt
            caminho_arquivo = os.path.join(pasta_ncb, nome_arquivo)
            if nome_arquivo in ids_nomes:
                novo_header = f">{ids_nomes[nome_arquivo]}\n"
                novo_caminho = os.path.join(pasta_ncb, f"{ids_nomes[nome_arquivo]}.txt")  # Alterar para .txt
                
                # Lê o conteúdo original
                with open(caminho_arquivo, 'r') as file:
                    linhas = file.readlines()
                
                # Substitui o header
                with open(caminho_arquivo, 'w') as file:
                    file.write(novo_header)
                    file.writelines(linhas[1:])
                
                # Renomeia o arquivo
                if caminho_arquivo != novo_caminho:
                    os.rename(caminho_arquivo, novo_caminho)
                print(f'Atualizado e renomeado: {caminho_arquivo} -> {novo_caminho}')

# Caminhos dos arquivos
csv_arquivo = r"C:\Users\Cliente\Desktop\mitogenome\Scripts\submission_ncbi\features_2309.csv"
pasta_ncb = r"C:\Users\Cliente\Desktop\NCBI"

atualizar_headers(csv_arquivo, pasta_ncb)
