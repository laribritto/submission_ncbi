import os
from Bio import SeqIO  # Importando o módulo SeqIO do Biopython

# Caminho para a pasta com os arquivos fasta
root_dir = r"C:\Users\Cliente\Desktop\mitogenome\fasta_mitofish"  # Altere para o caminho correto

# Função para extrair Genero e Especie do nome do arquivo
def extract_genus_species(filename):
    parts = filename.split('_')
    if len(parts) >= 3:
        genero = parts[1]
        especie = parts[2].replace('.fa', '')
        return f"{genero} {especie}"
    else:
        print(f"Nome de arquivo inesperado: {filename}")
        return None

# Função para modificar o header dos contigs
def modify_fasta_headers(input_file, code, genus_species):
    temp_file = input_file + ".tmp"  # Arquivo temporário para evitar problemas com leitura e escrita simultânea
    with open(temp_file, 'w') as output_handle:
        for record in SeqIO.parse(input_file, "fasta"):
            new_header = f"{code} [organism={genus_species}] {genus_species} mitochondrion, complete genome"
            record.id = new_header
            record.description = ""
            SeqIO.write(record, output_handle, "fasta")
    os.replace(temp_file, input_file)  # Substitui o arquivo original pelo arquivo temporário
    print(f"Arquivo sobrescrito: {input_file}")

# Contador inicial
contig_number = 1

# Loop para ler recursivamente os arquivos fasta
for subdir, dirs, files in os.walk(root_dir):
    for file in files:
        if file.endswith('.fa'):  # Verifica se é um arquivo fasta
            input_fasta = os.path.join(subdir, file)
            genus_species = extract_genus_species(file)
            
            if genus_species:  # Se conseguiu extrair o gênero e espécie
                code = f"AG{contig_number:03d}"  # Formato AG001, AG002, etc.
                
                # Modifica os headers dos contigs e sobrescreve o arquivo original
                modify_fasta_headers(input_fasta, code, genus_species)
                
                # Imprime uma mensagem informando que a modificação foi feita
                print(f"Modificação feita no arquivo: {file}")
                
                # Incrementa o número do contig
                contig_number += 1
            else:
                print(f"Erro ao processar o arquivo: {file}")

print("Todas as modificações foram concluídas!")
