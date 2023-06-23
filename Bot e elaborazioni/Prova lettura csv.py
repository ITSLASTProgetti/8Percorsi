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


from telegram.ext import *
from telegram import *
import geocoder

# Funzione per gestire il comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id=chat_id, text="Ciao! Invia il comando /coordinate per ottenere le tue coordinate.")

# Funzione per gestire il comando /coordinate
async def coordinates(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    location = update.message.location

    latitude = location.latitude
    longitude = location.longitude

    context.bot.send_message(chat_id=chat_id, text=f"Le tue coordinate sono: Latitudine: {latitude}, Longitudine: {longitude}")

# Funzione principale
async def main():
    # Inizializza il bot con il token fornito dal BotFather
    token = '6000000744:AAH-QS8U829fadQwj2EhMVlq4E_GgblQymA'
    updater = Updater(token)

    # Ottieni il dispatcher per registrare gli handler dei comandi
    dispatcher = updater.dispatcher

    # Aggiungi gli handler per i comandi
    start_handler = CommandHandler('start', start)
    coordinates_handler = CommandHandler('coordinate', coordinates)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(coordinates_handler)

    # Avvia il bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()"""
"""
