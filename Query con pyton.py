
import csv

# Nome del file CSV da leggere
csv_file = 'Percorsi_Pastrengo.csv'

# Lista per salvare le righe del file CSV
data_list = []
query_result=[]
# Apri il file CSV in modalità lettura
with open(csv_file, 'r') as file:
    reader = csv.reader(file, delimiter=';')
                        
    # Itera attraverso le righe del file CSV e salva ciascuna riga nella lista
    for row in reader:
        data_list.append(row)

# Stampa la lista delle righe del file CSV
#for row in data_list:
    # print(row)
A=input("dammi una distanza")
print(A)
for row in data_list:
    if row[4] >= A:
        query_result.append(row)

print(query_result)
