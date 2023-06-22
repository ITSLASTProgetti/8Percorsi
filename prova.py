# import logging
# from telegram import __version__ as TG_VER

"""
try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]

if __version_info__ < (20, 0, 0, "alpha", 1):
    raise RuntimeError(
        f"This example is not compatible with your current PTB version {TG_VER}. To view the "
        f"{TG_VER} version of this example, "
        f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
    )
    """

from telegram import ForceReply, Update, Chat
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

# Enable logging
"""
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)
"""
# Define a few command handlers. These usually take the two arguments update and
# context.

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.message
    text = update.message.text
    id = update.message.chat.id

    if update.message.location:
        lat = message.location.latitude
        lon = message.location.longitude
        # location = message.location

        # una volta trovata una LOCATION dovete usare una funzione per scorrere i vostri dataset/database
        # cercate l'oggetto più vicino alla vostra posizione (con il codice che trovate sul gruppo Telegram)
        # restituite in output nel prossimo await update.message.reply_venue con la lat e lon dell'oggetto, Nome e Via

        # qui prendete i valori di NomeOggetto e NomeVia dal vostro DB
        await update.message.reply_venue(lat, lon, 'NomeOggetto', 'NomeVia?')

        #await update.message.reply_text(lat)
        #await update.message.reply_text(lon)
        #handle_location(id, message.location)

    else:
        await update.message.reply_text('Mandami una posizione')

    await update.message.reply_text(id)


"""
async def position(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    Get user position when /position is issued. Send me your position
    user_position = send_location(Chat.id)
    await update.message.reply_text(user_position)

async def handle_location(id, location):
    latitude = message.location.latitude
    longitude = message.location.longitude
    await update.message.reply_text(text="Your coordinates: Latitude {}, Longitude {}".format(latitude, longitude))
"""

def main() -> None:
    """Start the bot."""
    # Crare l'applicazione (il vostro bot)
    application = Application.builder().token('!!!INSERITE QUI IL TOKEN DEL VOSTRO BOT!!!').build()

    # Aggiungi un handler per il comando /start
    application.add_handler(CommandHandler("start", start))

    # Controlla tutti i messaggi inviati, se il messaggio inviato è una LOCATION, fai partire la funzione handle_message
    application.add_handler(MessageHandler(filters.LOCATION, handle_message))

    # Run the bot until the user presses Ctrl-C
    application.run_polling()

if __name__ == "__main__":
    main()
