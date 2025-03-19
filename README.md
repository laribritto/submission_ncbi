# Pipeline for Preparing Files for NCBI Submission  

This workflow organizes and processes **FASTA** and **.NCBI** files to meet NCBI submission requirements.  

## Steps:  

### 1. Separate `.NCBI` and `.fa` files  
Ensure that **.NCBI** annotation files and **.fa** sequence files are stored in separate directories.  

### 2. Assign a temporary name  
Each sequence is assigned a temporary identifier in the format `AG*` (e.g., **AG001, AG002, ...**).  

### 3. Update `.NCBI` files with the new temporary name  
Use the **`update_headers.py`** script to modify `.NCBI` files, replacing old names with the new identifier.  

### 4. Create a consolidated FASTA file  
Run the following command to generate a single file containing all sequences:  
```bash
cat *.fa > mitochondrion.fa
```

### 5. Merge all annotation files into a single **`features.txt`** file:
To combine all `.NCBI` annotation files, use:
```bash
cat *.txt > features.txt
```

### 6. Modify FASTA headers to match the NCBI format
The **`modify_fasta_headers.py`** script updates FASTA headers to the required format:
```bash
>AG089 [organism=Arapaima gigas] Arapaima gigas mitochondrion, complete genome
```

After completing these steps, the files will be ready for NCBI submission of mitochondrial sequence. 
