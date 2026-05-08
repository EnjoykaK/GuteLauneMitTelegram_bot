from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
TOKEN = "8788699632:AAECzdTbn-r7pesobmtN7hjSctVvfy1U6t8"
async def start(update: Update, context: ContextTypes. DEFAULT_TYPE):
    await update.message.reply_text("Hallo! Ich bin dein Bot für Gute Laune! :)")
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
