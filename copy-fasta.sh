mkdir -p /mnt/c/Users/Cliente/Desktop/mitogenome/Scripts/submission_ncbi/NCBI  # Cria a pasta fasta se não existir

find /mnt/c/Users/Cliente/Desktop/mitogenome/mitofish-novoplasty -type f -name '*.NCBI.txt' -exec cp {} /mnt/c/Users/Cliente/Desktop/mitogenome/Scripts/submission_ncbi/NCBI/ \;
