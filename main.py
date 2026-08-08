import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("TOKEN")

if not TOKEN:
raise RuntimeError("TOKEN is not set")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE): await update.message.reply_text("Bot is running successfully!")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.run_polling()
