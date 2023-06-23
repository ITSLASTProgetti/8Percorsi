from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import exchangelib
import csv
 
with open("token.txt", "r") as f:
    TOKEN = f.read()
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE)->None:
    await update.message.reply_text("Ciao vuoi sapere sul nostro bot allora esegui il comando /info")
        

    
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""Comandi disponibili:
        /start
        /Info: scegli un numero
        /query: Scegli il il percorso 
        """)

async def query(update: Update, context: ContextTypes.DEFAULT_TYPE)->None:



    prima_stringa = context.args[0]
    seconda_stringa = context.args[1]

    print("la prima stringa è ", prima_stringa)
    print("la seconda stringa è", seconda_stringa)
    seconda_stringa=float(seconda_stringa)
    
    csv_file = 'Percorsi_Pastrengo.csv'

    # Lista per salvare le righe del file CSV
    data_list = []
    lista = []
    query_result=[]
    # Apri il file CSV in modalità lettura
    with open(csv_file, 'r') as file:
        reader = csv.reader(file, delimiter=';')                       
        # Itera attraverso le righe del file CSV e salva ciascuna riga nella lista
        for row in reader:
            print(row)
            row[5]=float(row[5])
            data_list.append(row)
    
        for row in data_list:
            if row[0] == prima_stringa:
                if row[5]>= seconda_stringa:
                    query_result.append(row)
    try:
        for row in query_result:
            lista.append("Nome :" + row[1] + '\n' + "Tipo:" + row[3] + '\n' +" Lunghezza:"+str(row[5])+'\n'+'\n')
        
    except NameError as error:
        await update.message.reply_text("Non ci sono percorsi più lunghi di quello selezionato"+error)   

    finally:
        result_list = lista
        message = ''. join(result_list)
        await update.message.reply_text(message)

async def Info(update: Update, context: ContextTypes.DEFAULT_TYPE)->None:
        await update.message.reply_text("Inserire i due dati separati da uno spazio usare il comando /Query Es. / Query Pastrengo 7 ")
        await update.message.reply_text("Ricerca nel territorio selezionato e con distanza maggiore di quella selezionata")
def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('help', help))
    app.add_handler(CommandHandler('Info', Info))
    app.add_handler(CommandHandler("query",query))
    
    app.run_polling()

 
if __name__=='__main__':
   main()



"""

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
"""
