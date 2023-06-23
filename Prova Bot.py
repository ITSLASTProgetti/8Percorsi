from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import exchangelib
import csv
 
with open("token.txt", "r") as f:
    TOKEN = f.read()
    print("Il tuo token è", TOKEN)
    
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""Comandi disponibili:
        /Numero: scegli un numero
        /Query: scegli un numero  
        """)

"""async def Numero(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
     user_input =update.message.text
     print(user_input)
     update.message.reply_text(user_input)
"""
async def Query(update: Update, context: ContextTypes.DEFAULT_TYPE)->None:
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


    # Stampa la lista delle righe del file CSV
    #for row in data_list:
        #print(row)
    A=7
    B="Pastrengo"
    
    for row in data_list:
        if row[0] == B:
            if row[5]>= A:
                query_result.append(row)

    for row in query_result:
        lista.append("Nome :" + row[1] + '\n' + "Tipo:" + row[3] + '\n')
    
    csv_file.close()
    result_list = lista
    message = ''. join(result_list)
    await update.message.reply_text(message)
    
def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler('help', help))
    app.add_handler(CommandHandler("Query",Query))
    
    app.run_polling()

 
if __name__=='__main__':
   main()
