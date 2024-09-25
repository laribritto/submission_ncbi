import pandas as pd


df = pd.read_csv(r"C:\Users\Cliente\Desktop\mitogenome\Scripts\submission_ncbi\features_2309.csv")

df['Nome_Arquivo'] = df['Nome_Arquivo'].str.split('_').str[0]

df.columns = ['Sequence_ID', 'Accession']

df.to_csv(r"C:\Users\Cliente\Desktop\mitogenome\Scripts\submission_ncbi\at_features_2309.tsv", sep='\t', index=False)