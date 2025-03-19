import os
from Bio import SeqIO  # Importing the SeqIO module from Biopython

# This script processes FASTA files, modifies sequence headers by adding a unique identifier,
# extracts genus and species from the filename, and overwrites the original files with updated headers.

# Path to the directory containing FASTA files
root_dir = r"C:\Users\Cliente\Desktop\mitogenome\fasta_mitofish"  # Change to the correct path

# Function to extract Genus and Species from the filename
def extract_genus_species(filename):
    parts = filename.split('_')
    if len(parts) >= 3:
        genus = parts[1]
        species = parts[2].replace('.fa', '')
        return f"{genus} {species}"
    else:
        print(f"Unexpected filename format: {filename}")
        return None

# Function to modify FASTA headers
def modify_fasta_headers(input_file, code, genus_species):
    temp_file = input_file + ".tmp"  # Temporary file to avoid simultaneous read/write issues
    with open(temp_file, 'w') as output_handle:
        for record in SeqIO.parse(input_file, "fasta"):
            new_header = f"{code} [organism={genus_species}] {genus_species} mitochondrion, complete genome"
            record.id = new_header
            record.description = ""
            SeqIO.write(record, output_handle, "fasta")
    os.replace(temp_file, input_file)  # Replace the original file with the modified version
    print(f"File overwritten: {input_file}")

# Initial counter for unique sequence IDs
contig_number = 1

# Loop through all subdirectories and files in the root directory
for subdir, dirs, files in os.walk(root_dir):
    for file in files:
        if file.endswith('.fa'):  # Check if the file is a FASTA file
            input_fasta = os.path.join(subdir, file)
            genus_species = extract_genus_species(file)
            
            if genus_species:  # Proceed only if Genus and Species were extracted successfully
                code = f"AG{contig_number:03d}"  # Format AG001, AG002, etc.
                
                # Modify the headers and overwrite the original file
                modify_fasta_headers(input_fasta, code, genus_species)
                
                # Print confirmation message
                print(f"Modification completed for file: {file}")
                
                # Increment the contig number for the next file
                contig_number += 1
            else:
                print(f"Error processing file: {file}")

print("All modifications completed!")
