import os
import csv

"""
This script updates the headers of text files based on a CSV file containing sequence IDs and filenames. 
It replaces the first line of each matching file with the new header and renames the file accordingly. 
The updated files are stored in the specified directory, maintaining their original content except for the header.
"""

def update_headers(csv_file, ncbi_folder):
    # Read sequence IDs and filenames from the CSV file
    ids_names = {}  # Dictionary to store {filename: sequence_id}
    
    # Open the CSV file and read the data
    with open(csv_file, 'r') as csvfile:
        reader = csv.reader(csvfile)  # Initialize the CSV reader
        next(reader)  # Skip the header line

        # Iterate over each row in the CSV file
        for row in reader:
            if len(row) == 2:  # Ensure the row has exactly two columns
                sequence_id, filename = row  # Extract sequence ID and filename
                ids_names[filename] = sequence_id  # Store in the dictionary
    
    # Iterate through files in the specified folder
    for filename in os.listdir(ncbi_folder):
        if filename.endswith('.txt'):  # Process only .txt files
            file_path = os.path.join(ncbi_folder, filename)  # Get the full file path
            
            # Check if the file is listed in the dictionary
            if filename in ids_names:
                new_header = f">{ids_names[filename]}\n"  # Create the new FASTA-style header
                new_path = os.path.join(ncbi_folder, f"{ids_names[filename]}.txt")  # Define the new filename
                
                # Read the original content of the file
                with open(file_path, 'r') as file:
                    lines = file.readlines()  # Read all lines
                
                # Overwrite the file with the new header and retain the rest of the content
                with open(file_path, 'w') as file:
                    file.write(new_header)  # Write the new header
                    file.writelines(lines[1:])  # Keep the rest of the file, skipping the old header
                
                # Rename the file if the name has changed
                if file_path != new_path:
                    os.rename(file_path, new_path)  # Rename the file
                print(f'Updated and renamed: {file_path} -> {new_path}')  # Print confirmation message

# Define file paths
csv_file = r"C:\Users\Cliente\Desktop\mitogenome\Scripts\submission_ncbi\features_2309.csv"
ncbi_folder = r"C:\Users\Cliente\Desktop\NCBI"

# Call the function to update headers and rename files
update_headers(csv_file, ncbi_folder)
