
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
        row[5]=float(row[5])
        data_list.append(row)

print(data_list)
# Stampa la lista delle righe del file CSV
#for row in data_list:
    #print(row)
A=float(input("dammi una distanza"))
B=str(input("Dammi un Paese"))
print(A)
for row in data_list:
    if row[0] == B:
        if row[5]>= A:
            query_result.append(row)

print(query_result)

