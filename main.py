aus Telegram importieren Aktualisieren
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8368407308:AAGoOw3pKbXGNk8y1w6uH-7ceHrIhh-GRuQ"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
await update.message.reply_text("Bot läuft erfolgreich!")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.run_polling()
