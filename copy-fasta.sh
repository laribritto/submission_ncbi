#!/bin/bash

# This script copies specific .fa files from a source directory to a destination folder.
# It logs copied and missing files, identifies folders where files were not copied, 
# and generates reports for further verification.

# Create the destination folder if it doesn't exist
mkdir -p /mnt/c/Users/Cliente/Desktop/mtdna-fastas

# Find and copy .fa files that do NOT end with "_genes.fa" to the destination folder
find /mnt/c/Users/Cliente/Desktop/mitogenome/mitofish-novoplasty -type f -name '*.fa' ! -name '*_genes.fa' -exec cp {} /mnt/c/Users/Cliente/Desktop/mtdna-fastas/ \;

# List all .fa files that should have been copied
find /mnt/c/Users/Cliente/Desktop/mitogenome/mitofish-novoplasty -type f -name '*.fa' ! -name '*_genes.fa' > arquivos_a_copiar.txt

# List the files that were actually copied to the destination folder
ls /mnt/c/Users/Cliente/Desktop/mtdna-fastas/ > arquivos_copiados.txt

# Identify files that were not copied
grep -Fxvf arquivos_copiados.txt arquivos_a_copiar.txt > arquivos_nao_copiados.txt

# List all directories containing .fa files
find /mnt/c/Users/Cliente/Desktop/mitogenome/mitofish-novoplasty -type d > pastas_com_arquivos.txt

# Create an empty file to store directories where no files were copied
> pastas_nao_copiadas.txt

# Check each folder to see if any files were copied from it
while IFS= read -r pasta; do
    # Count the .fa files in the folder that should have been copied
    arquivos_na_pasta=$(find "$pasta" -maxdepth 1 -type f -name '*.fa' ! -name '*_genes.fa' | wc -l)
    
    # Count the copied files corresponding to this folder
    arquivos_copiados_na_pasta=$(basename "$pasta")_fa_count=$(ls /mnt/c/Users/Cliente/Desktop/mtdna-fastas/ | grep "^$(basename "$pasta")_" | wc -l)

    # If no files were copied from this folder but there were files to be copied, add it to the list
    if [ "$arquivos_copiados_na_pasta" -eq 0 ] && [ "$arquivos_na_pasta" -gt 0 ]; then
        echo "$(basename "$pasta")" >> pastas_nao_copiadas.txt
    fi
done < pastas_com_arquivos.txt

# Display the results
echo "Files that were not copied:"
cat arquivos_nao_copiados.txt

echo "Folders that had no files copied:"
cat pastas_nao_copiadas.txt
